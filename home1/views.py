from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Job_information,Job_information1,Jobshow,contactus
from django.core.mail import send_mail
from django.conf import settings




@login_required(login_url='loginn')
def home(request):
  
  return render(request,'index/index.html')


# def save(request):
#       if request.method== 'POST':

#          phone = request.POST.get('phone')
#          state = request.POST.get('state')
#          city = request.POST.get('city')
#          zipcode = request.POST.get('zipcode')
#          qualification = request.POST.get('qualification')
#          experience = request.POST.get('experience')

#          sf=save_form(phone=phone,
#                       state=state,
#                       city=city,
#                       zipcode=zipcode,
#                       Qualification=qualification,
#                       Experience=experience)
#          sf.save()

         


#       return render(request,'')



def contact(request):
      if request.method== 'POST':

         cname = request.POST.get('name')
         cemail = request.POST.get('email')
         cmessage = request.POST.get('message')

         sf=contactus(name=cname,
                      email=cemail,
                      message=cmessage)
         
         sf.save()
         print(cname,cemail,cmessage)
         


      return render(request,'index/contact.html')  


    
def loginn(request):
   if request.method == 'POST':

      lusername = request.POST.get('lusername')
      lpassword = request.POST.get('lpassword')
      user = authenticate(request, username=lusername, password=lpassword)

      if user is not None:
         login(request, user)
         return render(request,'index/index.html')
        
      else:
         return render(request, 'base/login.html')
      
   return render(request, 'base/login.html')

def signinn(request):
  if request.method =='POST':

    firstname=request.POST.get('firstname')
    lastname=request.POST.get('lastname')
    username=request.POST.get('username')
    semail=request.POST.get('email')
   
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
    



  return render(request,'base/signup.html')

@login_required(login_url='loginn')
# greencodes
def inside(request):
   jobgarana=Job_information1.objects.all()
   context1={'jobgarana':jobgarana}
   return render(request,'index/index1.html',context1)



@login_required(login_url='loginn')
# cedargrate
def inside1(request):
   jobgara=Job_information.objects.all()
   context={'jobgara':jobgara}
   return render(request,'index/index2.html',context)



def inside2(request):
   jobdekhaus=Jobshow.objects.all()
   # print(jobdekhaus)
   context2={'jobdekhau':jobdekhaus}
   return render(request,'index/jobs.html',context2)








def logoutt(request):
   logout(request)
   return render(request,'base/login.html')


@login_required(login_url='loginn')
def apply(request):
   
   return render(request,'index/index3.html')


def submit(request): 
   return HttpResponse('Thank you We will reach you soon')
   
@login_required(login_url='loginn')
def about(request):
   return render(request,'index/about.html')

@login_required(login_url='loginn')


# def contact(request):
#    return render(request,'index/contact.html')

def jobs(request):
   return render(request,'index/jobs.html')





  

   

    





  
















