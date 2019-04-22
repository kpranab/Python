from .models import Task
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task_name', 'task_desc')
