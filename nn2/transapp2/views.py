from django.shortcuts import render
from .serializers import TransSerializers2
from .models import TransModel2
from .prmission import TransPermission2
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.
class TransAll2(generics.ListAPIView):
    queryset = TransModel2.objects.all()
    serializer_class = TransSerializers2

    def get_queryset(self):
        return TransModel2.objects.all()
    
class CreateTrans2(generics.CreateAPIView):
    queryset = TransModel2.objects.all()
    serializer_class = TransPermission2

class UpdataTrans2(generics.RetrieveUpdateDestroyAPIView):
    queryset =  TransModel2.objects.all()
    serializer_class = TransSerializers2
    permission_classes = (IsAuthenticated,TransPermission2)

