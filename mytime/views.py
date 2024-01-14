#from django.http import HttpResponse
#  return HttpResponse("Welcome to the about page")
from django.shortcuts import render
from mytime import models

def homepage(request):
    time_entries = models.TimeEntry.objects.all()
    context = {"time_entries": time_entries}
    return render(request,'mytime/home.html', context)

def about(request):
    return render(request,'mytime/about.html')
