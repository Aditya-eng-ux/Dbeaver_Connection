"""Main URL configuration for the project"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, PostViewSet
from api.views import api_home

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', api_home, name='api-home'),
    path('api/', include(router.urls)),
]
