from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
# from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
  
  return render(request,'index.html')
    #  return HttpResponse("hey this is ritesh kafle")


    
def loginn(request):
    if request.method == 'POST':
        hemail = request.POST.get('username')
        hpassword = request.POST.get('lpassword')
        user = authenticate(request, username=hemail, password=hpassword)

        if user is not None:
            login(request, user)
            return render(request,'index/index.html')
        else:
            return render(request, 'base/login.html', {'error_message': 'Incorrect Username/Password'})

    return render(request, 'base/login.html')

def signinn(request):
  if request.method =='POST' :

    firstname=request.POST.get('firstname')
    lastname=request.POST.get('lastname')
    username=request.POST.get('username')
    semail=request.POST.get('semail')
    spassword1=request.POST.get('spassword1')
    spassword2=request.POST.get('spassword2')


    if spassword1 != spassword2:
            return HttpResponse('password donot match')
    elif User.objects.filter(username=username ).exists():
     return HttpResponse("username already exist")
    else:
      my_user=User.objects.create_user(username,semail,spassword1)
      my_user.first_name=firstname
      my_user.last_name=lastname
      my_user.save()

    return HttpResponse('Account has been Created Successfully')
    

    # print(firstname,lastname,username,email,password1,password2)

  return render(request,'base/signup.html')







  

   

    





  # else :
  #   return HttpResponse('Error 404')

















