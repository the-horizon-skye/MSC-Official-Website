from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#for the main events page -- /events/
def home(request):
    return HttpResponse('You are in Events page')


# for the registeration page -- /events/register/
def register(request):
    return HttpResponse('You are in registration page')