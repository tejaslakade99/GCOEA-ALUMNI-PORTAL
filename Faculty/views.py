from django.shortcuts import render
from Accounts.models import *
# Create your views here.
def faculty(request):
    hod = AdminProfile.objects.all()
    pro = FacultyProfile.objects.all()
    context={'hod':hod,'pro':pro}
    return render(request,'Faculty/faculty.html',context)