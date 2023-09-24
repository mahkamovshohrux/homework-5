from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class TransModel1(models.Model):
    task_name = models.CharField(max_length=30,default="")
    create = models.DateTimeField(default=datetime.now)
    update = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=200,default="")
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.task_name
    class Meta:
        db_table = 'trans1'