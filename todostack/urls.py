from django.urls import path, include
from .views import *


urlpatterns = [
    path('', start, name="ToDo-Stack Start!"),
    path('start', start, name="ToDo-Stack Start!"),
    path('manage', manage, name="ToDo-Stack Manage"),
    path('work', work, name="Work!")
]