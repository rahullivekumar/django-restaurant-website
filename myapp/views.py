from django.shortcuts import render,redirect
from  django.template import loader
from  django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from myapp.form import *
from .models import Reserve
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db import IntegrityError
from django.core.validators import ValidationError
from datetime import date
from  django.core.mail import send_mail
from javat import settings

def index(request):
    stu=StudentForm()
    return render(request,'index.html',{'form':stu})


def register(request):
    print("ty")
    if request.method == "POST":

        username=request.POST['username']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if len(username)==0:
            messages.info(request, 'Username can not  be empty')
            return redirect('register')
        elif len(first_name)==0:
            messages.info(request, 'First_name can not  be empty')
            return redirect('register')
        elif len(email)==0:
            messages.info(request, 'Email field can not  be empty')
            return redirect('register')
        elif len(password1) < 5:
            messages.info(request, 'Password can not  be empty or its length can not be less than 5 ')
            return redirect('register')

        elif password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username= username,password=password1,last_name=last_name,first_name=first_name,email=email)
                try:

                    subject = "Greetings"
                    msg = "welcome to our resraurant"
                    to= email
                    res = send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
                    if res==1:
                        messages.info(request, "Email is send to ur Eamil Id")
                        user.save()
                    else:
                        print('nope')
                except:
                    messages.info(request,"Cant send mail but user is created")
                    user.save()
                    print("no internet")
                print("hellooooo")
                return redirect('login')
        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Username/Password')
            return redirect('login')
    else:
        return render(request,'login.html')

def css3(request):
    return render(request,'css3.html')

def logout(request):
    auth.logout(request);
    return redirect('home')

def reserve(request):
    if request.method == "POST":
        try:
            r=Reserve()
            r.name = request.POST.get('name')
            r.dt =  request.POST.get('dt')
            today= date.today()
            r.tt = request.POST.get('tt')
            r.tableno = request.POST.get('tableno')
            r.email = request.POST.get('email')
            r.phone = request.POST.get('phone')
            if len(r.name)==0:
                messages.info(request, 'Name can not  be empty')
                return redirect('reserve')
            elif len(r.phone) != 10:
                messages.info(request, 'Enter valid phone Number')
                return redirect('reserve')

            try:
                subject = "YOUR TABLE IS RESERVED"
                msg = " name: " + r.name + "\n date : " + str(r.dt) + "\n time :  " + r.tt + "\n table no :" + str(r.tableno)
                to = r.email
                r.save()
                res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
                if res == 1:
                    print("internet")
                else:
                    return redirect("reserve")
            except:
                r.save()
                print("no internet")
            return redirect('home')
        except IntegrityError:
            messages.info(request,'This Table is not vacant at this moment')
            return redirect('reserve')
        except ValidationError:
            messages.error(request,"Enter Valid Date")
            return redirect('reserve')
        #except TypeError:
         #   messages.info(request, 'Enter Valid Date')
          #  return redirect('reserve')


    return render(request,'reserve.html')


# Create your views here.
