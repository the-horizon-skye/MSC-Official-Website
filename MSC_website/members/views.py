from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# for the members page -- /members/
def home(request):
    return HttpResponse('You are in Members')

# for the gallery in members -- /members/gallery/
def gallery(request):
    return HttpResponse('You are in gallery')
