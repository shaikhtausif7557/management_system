from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'updated_at','created_by']  # Exclude 'created_by'

class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'created_at','created_by']  # Exclude 'created_by'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']