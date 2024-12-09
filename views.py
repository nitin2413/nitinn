from django.shortcuts import render, redirect
from home.models import Contact
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
def index(request):
    # context = {
    #       "variable1": "nitin is great",
    # }
    messages.success(request,f"Welcome, {request.user.username}!")#string formatting
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
    #return HttpResponse("this is homepage made my nass")

def sign_up(request):
    if request.method == "POST": # ager form post huaa hai tho ye code render hoga
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request,"password do not match!")
            return redirect("sign_up")

        if User.objects.filter(username=username).exists():
            messages.error(request,"this user name already exist, try adding @#$ in username")
            return redirect("sign_up")

        if User.objects.filter(email=email).exists():
            messages.error(request, "this email is in use")
            return redirect("sign_up")

        user = User.objects.create_user(username=username,email=email,password=password )
        user.save()
        messages.success(request,"your account is created")
        return redirect("/login")
    return render(request,'sign_up.html')


    # return render(request, 'signin.html')

def loginUser(request):
    # check if user has entered correct credentials

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page made my nass")
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is servicespage made my nass")

def contact(request):
    if request.method == "POST": # ager form post huaa hai tho ye code render hoga
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, "your massage has been sent.")
    return render(request, 'contact.html')


