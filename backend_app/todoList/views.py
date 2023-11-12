from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import todoModel

# urls.py とのつなぎこみ
class TodoList(ListView):   # LIstViewの継承
    template_name = 'list.html'
    # tデータに渡すテーブルの指定
    model = todoModel