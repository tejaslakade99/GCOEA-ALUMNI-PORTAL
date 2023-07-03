from django.urls import path
from .views import *
urlpatterns = [
    path('alumni-history/', alumni_history, name="alumni-history"),
]