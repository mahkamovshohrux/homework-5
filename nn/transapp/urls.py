from django.urls import path
from .views import (TransAll,CreateTrans,UpdataTrans)

urlpatterns = [
    path('all/', TransAll.as_view()),
    path('create/',CreateTrans.as_view()),
    path('update/',UpdataTrans.as_view())
]