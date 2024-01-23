from django.db import models

# Create your models here.

class Product(models.Model):
  # sno=models.AutoField() 
  first_name=models.CharField(max_length=40)
  last_name=models.CharField(max_length=40)
  phont_num=models.IntegerField()

