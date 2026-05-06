from django.contrib import admin
from .models import User, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for User model"""
    list_display = ('id', 'name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email')
    ordering = ('-created_at',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin configuration for Post model"""
    list_display = ('id', 'title', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'user')
    search_fields = ('title', 'content', 'user__name')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
