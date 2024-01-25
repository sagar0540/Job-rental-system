from django.db import models


# Create your models here.
# cedargate
class Job_information(models.Model):
  Job_Category=models.CharField(max_length=100)

  Job_Level=models.CharField(max_length=100)

  Job_Type=models.CharField(max_length=100)

  Job_Location=models.CharField(max_length=100,)

  Job_Vacanys=models.IntegerField()

  Job_Salary=models.IntegerField()

  Job_Deadline=models.DateTimeField()

  Job_Educationlevel=models.CharField(max_length=100)

  Job_Experience=models.CharField(max_length=100)

  def __str__(self):
    return self.Job_Category
  
# greencodes
class Job_information1(models.Model):
  Job_Category1=models.CharField(max_length=100)

  Job_Level1=models.CharField(max_length=100)

  Job_Type1=models.CharField(max_length=100)

  Job_Location1=models.CharField(max_length=100,)

  Job_Vacanys1=models.IntegerField()

  Job_Salary1=models.IntegerField()

  Job_Deadline1=models.DateTimeField()

  Job_Educationlevel1=models.CharField(max_length=100)

  Job_Experience1=models.CharField(max_length=100)
  Job_Skills1=models.CharField(max_length=100)

  def __str__(self):
    return self.Job_Category1
  







  

