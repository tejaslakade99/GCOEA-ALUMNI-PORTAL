from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from Accounts.models import Admin
from django.conf import settings
from django.core.mail import send_mail


def login_page(request):
    form = {}
    return render(request,'Accounts/login.html', form)


def select_role(request):

    if request.method == "POST":
        role = request.POST.get('role')
        if role == 'Hod':
            return redirect('register-admin')

    return render(request, 'Accounts/choice-page.html')


def register_admin(request):
    if request.method == "POST":
        pass

    return render(request,'Accounts/register.html', form)

def register_faculty(request):
    if request.method == "POST":
        pass

    return render(request, 'Accounts/register.html', form)

def register_alumni(request):
    if request.method == "POST":
        pass

    return render(request, 'Accounts/register.html', form)

# Create your views here.
