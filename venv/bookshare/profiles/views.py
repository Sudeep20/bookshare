from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,'profiles/bookshare.html')
