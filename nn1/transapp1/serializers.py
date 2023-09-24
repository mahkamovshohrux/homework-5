from rest_framework import serializers
from .models import TransModel1
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class TransSerializers1(serializers.ModelSerializer):
    class Meta:
        model = TransModel1
        fields =('task_name','create','update','status','description','user')

    def create(self, validated_data):
        validated_data["user"]= get_object_or_404(User,username=self.context['request'].user)
        return super(TransSerializers1,self).create(validated_data)