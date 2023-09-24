from django.shortcuts import render
from .serializers import TransSerializers
from .models import TransModel
from .permission import TransPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.
class TransAll(generics.ListAPIView):
    queryset = TransModel.objects.all()
    serializer_class = TransSerializers

    def get_queryset(self):
        return TransModel.objects.all()
    
class CreateTrans(generics.CreateAPIView):
    queryset = TransModel.objects.all()
    serializer_class = TransPermission

class UpdataTrans(generics.RetrieveUpdateDestroyAPIView):
    queryset =  TransModel.objects.all()
    serializer_class = TransSerializers
    permission_classes = (IsAuthenticated,TransPermission)

