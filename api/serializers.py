from rest_framework import serializers
from .models import User, Post


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'created_at', 'posts']
        read_only_fields = ['id', 'created_at']
    
    def get_posts(self, obj):
        posts = obj.posts.all()
        return PostSerializer(posts, many=True).data


class PostSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user', 'user_name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'user_name']
