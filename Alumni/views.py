from django.shortcuts import render
from Accounts.models import *
# Create your views here.


def alumni_history(request):
    alumni = AlumniProfile.objects.all()
    context = {'alumni': alumni}
    return render(request, 'Alumni/alumini-history.html', context)
