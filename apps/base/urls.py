from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.base import views

router = DefaultRouter()
router.register('task/', views.TaskApi, basename = 'task_api')

urlpatterns = [
    
]

urlpatterns += router.urls