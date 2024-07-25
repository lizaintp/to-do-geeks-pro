from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# Create your views here.

from apps.base import models
from apps.base import serializers

class TaskApi(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer