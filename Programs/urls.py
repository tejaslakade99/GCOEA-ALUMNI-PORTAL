from django.urls import path
from .views import *

urlpatterns = [
    path('contest/',contest,name="contest"),
    path('contest-form/',add_contest,name="add_contest"),
    path('events/',events,name="event"),
    path('event-form/', add_event, name="add_event"),
    path('delete-event/<slug:event_id>/', delete_event, name="delete_event"),
    path('delete-contest/<slug:contest_id>/', delete_contest, name="delete_contest"),
]