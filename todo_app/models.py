from django.db import models

# Create your models here.

class Todo(models.Model):
    no = models.IntegerField()
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200,null=True)
