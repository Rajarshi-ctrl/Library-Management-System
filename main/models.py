from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    auther = models.CharField(max_length=20, default="")
    desc = models.CharField(max_length=300, default="")
