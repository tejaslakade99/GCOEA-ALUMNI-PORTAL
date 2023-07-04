from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.


def about(request):
    return render(request, 'About/about.html')


def gallery(request):
    return HttpResponse("Hii Gallery")


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')

    return render(request, 'About/contact-us.html')
