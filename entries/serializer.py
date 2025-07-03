from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Entry, Tag, Profile


class TagSerializer(serializers.ModelSerializer):
    """
    class serializes Tag model
    """
    class Meta:
        model = Tag
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    """
    class serializes Entry model
    """
    author = serializers.StringRelatedField()
    tags = TagSerializer(many=True)
    class Meta:
        model = Entry
        fields = ('id', 'author', 'title', 'body', 'created_at', 'updated_at', 'is_archived', 'tags')

class UserSerializer(serializers.ModelSerializer):
    """
    class serializes User model
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')

class ProfileSerializer(serializers.ModelSerializer):
    """
    class serializes Profile model
    """
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'profile_pic')