from django.urls import path
from .views import (TransAll3,CreateTrans3,UpdataTrans3)

urlpatterns = [
    path('all/', TransAll3.as_view()),
    path('create/',CreateTrans3.as_view()),
    path('update/',UpdataTrans3.as_view())
]