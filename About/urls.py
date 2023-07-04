from django.urls import path
from .views import *


urlpatterns = [
    path('', about, name='about'),
    path('contact/', contact_us, name="contact us"),


]