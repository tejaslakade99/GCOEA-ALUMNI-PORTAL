from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request, 'About/about.html')

def gallery(request):
    return HttpResponse("Hii Gallery")

def contact(request):
    return HttpResponse("Hii Contact")