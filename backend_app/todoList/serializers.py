from rest_framework import serializers 
from todoList.models import todoModel
 
 
class todoModelSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = todoModel
        fields = ('id',
                  'title',
                  'description',
                  'published')