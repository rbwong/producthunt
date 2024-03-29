import json

from rest_framework import permissions, viewsets
from rest_framework import status, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from social.apps.django_app.utils import strategy

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):

    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


@strategy()
def auth_by_token(request, backend):
    backend = request.strategy.backend
    user = request.user
    user = backend.do_auth(
        access_token=request.DATA.get('access_token'),
        user=user.is_authenticated() and user or None
    )
    if user and user.is_active:
        return user  # Return anything that makes sense here
    else:
        return None


@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def social_register(request):
    auth_token = request.DATA.get('access_token', None)
    backend = request.DATA.get('backend', None)
    if auth_token and backend:
        try:
            user = auth_by_token(request, backend)
        except Exception, err:
            return Response(str(err), status=400)
        if user:
            strategy = load_strategy(request=request, backend=backend)
            _do_login(strategy, user)
            return Response("User logged in", status=status.HTTP_200_OK)
        else:
            return Response("Bad Credentials", status=403)
    else:
        return Response("Bad request", status=400)
