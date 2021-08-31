from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apioverview(request):
    api_urls={
        "list":'/task-list/',
        'detail view':'/task-detail/<str:pk>/',
        'create':'/task-create/',
        'task delete':'/task-delete/<str:pk>/',
        'task update':'/task-update/<str:pk>/'
 
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    task=Task.objects.all().order_by('-id')
    serializer=TaskSerializer(task,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(task,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskcreate(request):
    
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response('Item Deleted')