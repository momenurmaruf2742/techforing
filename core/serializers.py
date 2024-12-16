from rest_framework import serializers
from .models import User, Project, ProjectMember, Task, Comment

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'date_joined']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at']

# Project Member Serializer
class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ['id', 'project', 'user', 'role']

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.ReadOnlyField(source='assigned_to.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'task', 'created_at']
