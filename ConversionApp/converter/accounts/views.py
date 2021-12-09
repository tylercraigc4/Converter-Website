from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from converter_app import models
from accounts.forms import NewUserForm
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 

        user = auth.authenticate(username=username,password=password)

        if user is not None:
           auth.login(request, user)
           return redirect("/")
        else:
            messages.info(request, 'invalid crednetials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration Successful.')
            print("Registration Successful")
            return redirect('home')
        messages.error(request, 'unsuccessful registration. Invalid Information')
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form":form})


def homePage (request):
    return render (request, 'home.html')