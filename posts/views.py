from datetime import datetime, timedelta, time

from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework import generics, mixins

from posts.models import Country, Post
from posts.permissions import IsAuthorOfPost, IsAdmin
from posts.serializers import CountrySerializer, PostSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAdmin(),)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAuthorOfPost(),)

    def perform_create(self, serializer):
        country = Country.objects.get(pk=int(self.request.data['country']))
        instance = serializer.save(author=self.request.user, country=country)

        return super(PostViewSet, self).perform_create(serializer)

    def get_queryset(self):
        today = datetime.now().date()

        queryset = Post.today_objects.filter(
            is_approved=True).order_by('-created_at')
        days_ago = self.request.QUERY_PARAMS.get('days_ago', None)
        day = self.request.QUERY_PARAMS.get('day', None)

        if days_ago is not None:
            days_ago = int(days_ago)
            that_day = today - timedelta(days_ago)
            that_day = datetime.strftime(that_day, '%m-%d-%Y')
            queryset = Post.objects.filter(
                is_approved=True, day=that_day).order_by('-created_at')
        elif day is not None:
            queryset = Post.objects.filter(
                is_approved=True, day=day).order_by('-created_at')
        return queryset


class PostListAll(generics.ListAPIView):
    queryset = Post.objects.filter(is_approved=True).order_by('-created_at')
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 50
    serializer_class = PostSerializer


class AccountPostsViewSet(viewsets.ViewSet):
    queryset = Post.objects.filter(is_approved=True).select_related('author').all()
    serializer_class = PostSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
