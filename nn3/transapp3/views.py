from django.shortcuts import render
from .serializers import TransSerializers3
from .models import TransModel3
from .prmission import TransPermission3
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.
class TransAll3(generics.ListAPIView):
    queryset = TransModel3.objects.all()
    serializer_class = TransSerializers3

    def get_queryset(self):
        return TransModel3.objects.all()
    
class CreateTrans3(generics.CreateAPIView):
    queryset = TransModel3.objects.all()
    serializer_class = TransPermission3

class UpdataTrans3(generics.RetrieveUpdateDestroyAPIView):
    queryset =  TransModel3.objects.all()
    serializer_class = TransSerializers3
    permission_classes = (IsAuthenticated,TransPermission3)

