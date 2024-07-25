from rest_framework import serializers

from apps.base import models

class TaskSerializer(serializers.Serializer):
    class Meta:
        model = models.Task
        fields = ['id', 'title', 'description', 'created_at', 'completed']