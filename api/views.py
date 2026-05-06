from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import User, Post
from .serializers import UserSerializer, PostSerializer


@api_view(['GET'])
def api_home(request):
    """API home endpoint"""
    return Response({
        'message': 'Welcome to DBeaver Connection Project!',
        'version': '1.0',
        'endpoints': {
            'users': '/api/users/',
            'posts': '/api/posts/',
        }
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model
    Provides CRUD operations for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'email']
    ordering_fields = ['created_at', 'name']
    ordering = ['-created_at']


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Post model
    Provides CRUD operations for posts
    """
    queryset = Post.objects.all().select_related('user')
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__name']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
