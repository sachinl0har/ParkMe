from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
from users.models import userContact

# Create your views here.

def dashboard(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        return render(request, 'dashboard.html')

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = userContact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Message Sent Successfully!')
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.warning(request, 'Invalid Credentials.')
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username Already Exists.')
            return redirect("signup")
        else:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, 'Signup Successfull.')
            return redirect('dashboard')
    return render(request, 'signup.html')

def logoutUser(request):
    logout(request)
    return redirect("/")
    # return render(request, 'index.html')


