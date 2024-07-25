from django.contrib import admin
from apps.base import models

# Register your models here.
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'completed')
    list_filter = ('title', 'description', 'created_at', 'completed')