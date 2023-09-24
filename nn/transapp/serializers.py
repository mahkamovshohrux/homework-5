from rest_framework import serializers
from .models import TransModel
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class TransSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransModel
        fields =('task_name','create','update','status','description','user')

    def create(self, validated_data):
        validated_data["user"]= get_object_or_404(User,username=self.context['request'].user)
        return super(TransSerializers,self).create(validated_data)