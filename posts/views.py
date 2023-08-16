from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='posts:login')
def HomePage(request):
    return render(request, 'home.html')

def LoginPage(request):
    if request.method=='POST':
        uname= request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('posts:home')
        else:
            return HttpResponse("Incorrect Username or Password")

       # print(uname,password)

    return render(request, 'login.html')

def SignupPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pas = request.POST.get('password')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        myuser = User.objects.create_user(username=username,password=pas,email=email,first_name=fname,last_name=lname)
        myuser.save()
        return redirect('posts:login')
        #return HttpResponse("User has been created successfully.")
        #print (username,password,email,name)
    
    return render(request, 'signup.html')


def Logout(request):
    logout(request)
    return redirect('posts:login')