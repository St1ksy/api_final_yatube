from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


# Инициализация роутера для автоматической маршрутизации представлений
router = DefaultRouter()

# Регистрация маршрутов для работы с постами, группами, подписками и комментариями
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='followers')
router.register(r'^posts/(?P<post_pk>\d+)/comments', CommentViewSet,
                basename='comments'
                )

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
