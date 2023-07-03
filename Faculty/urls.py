from django.urls import path
from .views import *
urlpatterns = [
    path('faculty-members/',faculty,name="faculty"),
]