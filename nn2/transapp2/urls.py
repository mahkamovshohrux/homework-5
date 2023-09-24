from django.urls import path
from .views import (TransAll2,CreateTrans2,UpdataTrans2)

urlpatterns = [
    path('all2/', TransAll2.as_view()),
    path('create2/',CreateTrans2.as_view()),
    path('update2/',UpdataTrans2.as_view())
]