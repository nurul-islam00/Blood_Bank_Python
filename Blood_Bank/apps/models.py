from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50,blank=False,primary_key=True)
    password=models.CharField(max_length=50,blank=False)
    number=models.CharField(max_length=50,blank=False)
    sel1=models.CharField(max_length=50,blank=False)
    sel2=models.CharField(max_length=50,blank=False)


