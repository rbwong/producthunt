from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

from thinkster_django_angular_boilerplate.views import IndexView

from rest_framework_nested import routers

from authentication.views import AccountViewSet, LoginView, LogoutView
from posts.views import AccountPostsViewSet, PostViewSet, PostListAll, CountryViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'accounts', AccountViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'posts', PostViewSet, 'Post')

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account', trailing_slash=False
)
accounts_router.register(r'posts', AccountPostsViewSet)

urlpatterns = patterns(
     '',
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/v1/posts/all$', PostListAll.as_view(), name='all_posts'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
)
