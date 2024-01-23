from django.shortcuts import render,HttpResponse


# Create your views here.

def home(request):
  
  return render(request,'index/index.html')
    #  return HttpResponse("hey this is ritesh kafle")


def loginn(request):
  
  return render(request,'base/login.html')


def signinn(request):
  
  return render(request,'base/signup.html')
















