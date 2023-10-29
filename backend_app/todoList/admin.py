from django.contrib import admin
from .models import todoModel

# Register your models here.
# models.py のモデルを管理画面から操作できるようにする
admin.site.register(todoModel)