from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import MyFileUpload
from django.core.mail import send_mail


# Create your views here.
@login_required
def HomePage(request):
    if request.method == 'POST':
        file_name=request.POST.get('file_name')
        my_file=request.POST.get('my_file')

        new_file=MyFileUpload(file_name=file_name,my_file=my_file)
        new_file.save()
        return redirect("home-page")

    return render(request,'auth_system/index.html')
def Show(request):
        p=MyFileUpload.objects.all()
        return render(request,'auth_system/form.html',{'p':p})
 
def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name=request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        new_user = User.objects.create_user(name,email,password)
        new_user.first_name=fname
        new_user.last_name=lname
        new_user.save()
        return redirect('login-page')

    return render(request,'auth_system/register.html',{})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            send_mail(
                "Subject here",
                "Here is the message click this..http://127.0.0.1:8000/upload",
                "magudapathy1999@example.com",
                ["magudapathy.g@stanventures.com"],
                fail_silently=False,
            )
            return redirect('show-page')
            
        else:
            return HttpResponse('Error, user does not exist')
        

    return render(request,'auth_system/login.html')
def logoutuser(request):
    logout(request)
    return redirect('login-page')                                       





