from rest_framework import serializers

from apps.base import models

class TaskSerializer(serializers.Serializer):
    class Meta:
        model = models.Task
        fields = ['title', 'description', 'created_at', 'completed']