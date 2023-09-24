from django.urls import path
from .views import (TransAll1,CreateTrans1,UpdataTrans1)

urlpatterns = [
    path('all1/', TransAll1.as_view()),
    path('create1/',CreateTrans1.as_view()),
    path('update1/',UpdataTrans1.as_view())
]