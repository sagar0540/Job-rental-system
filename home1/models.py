from django.db import models


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

  
  
# greencodes
class Job_information1(models.Model):
  Job_Category1=models.CharField(max_length=100)

  Job_Level1=models.CharField(max_length=100)

  Job_Type1=models.CharField(max_length=100)

  Job_Location1=models.CharField(max_length=100)

  Job_Vacanys1=models.IntegerField()

  Job_Salary1=models.IntegerField()

  Job_Deadline1=models.DateTimeField()

  Job_Educationlevel1=models.CharField(max_length=100)

  Job_Experience1=models.CharField(max_length=100)
  Job_Skills1=models.CharField(max_length=100)


  #jobshow




# class save_form(models.Model):
#     phone=models.IntegerField()

#     state=models.CharField(max_length=100)

#     city=models.CharField(max_length=100)

#     zipcode=models.CharField(max_length=100)
#     Qualification=models.CharField(max_length=100)
#     Experience=models.CharField(max_length=100)
   
   

class contactus(models.Model):
    name=models.CharField(max_length=100)

    email=models.CharField(max_length=100)

    message=models.CharField(max_length=500)



class Jobshow(models.Model):
    Job_Title=models.CharField(max_length=100)

    Job_Description=models.CharField(max_length=100)
      
  
    

  
  







  

