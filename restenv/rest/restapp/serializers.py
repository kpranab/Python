from .models import Task
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Task
        fields = ('id', 'task_name', 'task_desc', 'completed','image')
