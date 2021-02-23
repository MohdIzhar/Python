from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

from datetime import datetime

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page serverd at " + str(datetime.now()))

def about(request):
    return HttpResponse("Hi, I'm Mohd Izhar and I am a software engineer.")