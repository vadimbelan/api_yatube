from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('', include(router.urls)),
]
