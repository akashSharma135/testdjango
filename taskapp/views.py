from django.db.models import fields
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Task
from todoapp.models import ManagerAssigned
from .serializers import TaskSerializer
from rest_framework.views import APIView
from django.core import serializers
from rest_framework import status
class TaskView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        
        task = Task.objects.create(assigned_task=request.data.get('task'))
        task.save()
        
        return Response({"msg": "Task Assigned!"}, status=status.HTTP_200_OK)