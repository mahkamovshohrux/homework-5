from django.shortcuts import render
from .serializers import TransSerializers1
from .models import TransModel1
from .permission import TransPermission1
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.
class TransAll1(generics.ListAPIView):
    queryset = TransModel1.objects.all()
    serializer_class = TransSerializers1

    def get_queryset(self):
        return TransModel1.objects.all()
    
class CreateTrans1(generics.CreateAPIView):
    queryset = TransModel1.objects.all()
    serializer_class = TransPermission1

class UpdataTrans1(generics.RetrieveUpdateDestroyAPIView):
    queryset =  TransModel1.objects.all()
    serializer_class = TransSerializers1
    permission_classes = (IsAuthenticated,TransPermission1)

