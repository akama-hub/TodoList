from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

from django.views.generic import ListView
from .models import todoModel

from rest_framework import status
 
from todoList.serializers import todoModelSerializer
from rest_framework.decorators import api_view

from rest_framework.views import APIView

# urls.py とのつなぎこみ

# api_view は関数型のビューの書き方
@api_view(['GET', 'POST', 'DELETE'])
def todo_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        todolists = todoModel.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            todolists = todolists.filter(title__icontains=title)

        todolists_serializer = todoModelSerializer(todolists, many=True)
        return JsonResponse(todolists_serializer.data, safe=False)  # 'safe=False' for objects serialization

    elif request.method == 'POST':
        todolist = JSONParser().parse(request)
        todolists_serializer = todoModelSerializer(data=todolist)
        
        if todolists_serializer.is_valid():
            todolists_serializer.save()
            return JsonResponse(todolists_serializer.data, status=status.HTTP_201_CREATED) 

        return JsonResponse(todolists_serializer.errors, statue=status.HTTP_400__BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = todoModel.objects.all().delete()
        return JsonResponse({'message': '{} todolists were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try: 
        todolist = todoModel.objects.get(pk=pk) 
    except todoModel.DoesNotExist: 
        return JsonResponse({'message': 'The content does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        todolists_serializer = todoModelSerializer(todolist) 
        return JsonResponse(todolists_serializer.data) 
 
    elif request.method == 'PUT': 
        todo_data = JSONParser().parse(request) 
        todolists_serializer = todoModelSerializer(todolist, data=todo_data) 
        if todolists_serializer.is_valid(): 
            todolists_serializer.save() 
            return JsonResponse(todolists_serializer.data) 
        return JsonResponse(todolists_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        todolist.delete() 
        return JsonResponse({'message': 'The content was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def todo_list_published(request):
    todolists = todoModel.objects.filter(published=True)
        
    if request.method == 'GET': 
        todolists_serializer = todoModelSerializer(todolists, many=True)
        return JsonResponse(todolists_serializer.data, safe=False)

class toDoListAPI(APIView):
    def get(self, request):
        todolists = todoModel.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            todolists = todolists.filter(title__icontains=title)

        todolists_serializer = todoModelSerializer(todolists, many=True)
        return JsonResponse(todolists_serializer.data, safe=False)  # 'safe=False' for objects serialization
    
    def post(self, request):
        todolist = JSONParser().parse(request)
        todolists_serializer = todoModelSerializer(data=todolist)
        
        if todolists_serializer.is_valid():
            todolists_serializer.save()
            return JsonResponse(todolists_serializer.data, status=status.HTTP_201_CREATED) 

        return JsonResponse(todolists_serializer.errors, statue=status.HTTP_400__BAD_REQUEST)
    
    def delete(self):
        count = todoModel.objects.all().delete()
        return JsonResponse({'message': '{} todolists were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    