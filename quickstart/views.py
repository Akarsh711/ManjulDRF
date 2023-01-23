from django.contrib.auth.models import User, Group
from .models import Todo
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from quickstart.serializers import UserSerializer, GroupSerializer, TodoSerializer
from rest_framework.response import Response



@api_view(['GET'])
def home(request):
    api_urls = {
        'List': 'todolist',
        'Create': 'createtodo',
        'Update': 'updatetodo',
        'Delete': 'deletetodo',
    }
    return Response(api_urls)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def taskList(request):
    # tasks = Todo.objects.filter(user_id = request.user)
    tasks = Todo.objects.all()
    serializer = TodoSerializer(tasks, many=True, context = {'fields':['id', 'name', 'done']})
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createTask(request):
    serializer = TodoSerializer(data = request.data, context = {'fields':['name', 'done', 'date_created']})
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def updateTask(request, pk):
    task = Todo.objects.get(id = pk)
    serializer = TodoSerializer(instance = task, data = request.data, context = {'fields':['id', 'name', 'done']})
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def deleteTask(request, pk):
    task = Todo.objects.get(id = pk)
    task.delete()
    return Response(request.user.id)


