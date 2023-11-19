from django.contrib import admin
from django.urls import path

from todoList import views 

urlpatterns = [
    #views.py ファイルを介してプロジェクトとのつなぎこみ
    # path('list/', TodoList.as_view()),
    # 正規表現 https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3
    path('api/todolists', views.todo_list),
    path('api/todolists/<pk>', views.todo_detail),
    path('api/todolists/published', views.todo_list_published)
]