from django.shortcuts import redirect, render
from django.contrib import messages
# from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from Accounts.models import *
from django.conf import settings


# Specifically Desgined Decorators
def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and AdminProfile.objects.filter(user_id=request.user.id).exists():
            return function(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrap


def faculty_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and FacultyProfile.objects.filter(user_id=request.user.id).exists():
            return function(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrap


def alumni_required(function):

    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and AlumniProfile.objects.filter(user_id=request.user.id).exists():
            return function(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrap


def student_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and StudentProfile.objects.filter(user_id=request.user.id).exists():
            return function(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrap


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user_obj = User.objects.filter(username=email, email=email)
        print(user_obj)
        if not user_obj:
            messages.warning(request, 'Account not found.')
            return redirect('Accounts/login.html')
        # if not user_obj[0].profile.is_email_verified:
        #     messages.warning(request, 'Your account in not verified.')
        #     return redirect('Accounts/login.html')
        print(email, password)
        user_login = authenticate(request=request, username=email, password=password)
        print(user_login)
        if user_login:
            login(request, user_login)
            return redirect("index")

        messages.success(request, 'Invalid credentials.')
        return redirect('index.html')

    return render(request, 'Accounts/login.html')


def select_role(request):
    if request.method == "POST":
        role = request.POST.get('role')
        return redirect('register-admin', my_role=role)
    return render(request, 'Accounts/choice-page.html')


def register_admin(request, my_role):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        branch = request.POST.get('branch')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        user_obj = User.objects.filter(email=email)
        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email,
                                            password=password)
        # user_obj.set_password(password)
        # user = None
        if my_role == 'Hod':
            user = AdminProfile.objects.create(user=user_obj, branch=branch)
        elif my_role == 'Faculty':
            user = FacultyProfile.objects.create(user=user_obj, branch=branch)
        elif my_role == 'Alumni':
            user = AlumniProfile.objects.create(user=user_obj, branch=branch)
        elif my_role == 'Student':
            user = StudentProfile.objects.create(user=user_obj, branch=branch)
        user.save()
        return HttpResponse("Success")

    return render(request, 'Accounts/register.html')


def index(request):
    return render(request, 'base.html')


