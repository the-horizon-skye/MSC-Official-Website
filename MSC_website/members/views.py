from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *


# Create your views here.

# for the members page -- /members/
def home(request):
    exec = Executive.objects.all()
    context = {
        'exec': exec,
        'header': 'Executives',
    }
    return render(request,'members/main.html',context)

# for the gallery in members -- /members/gallery/
def gallery(request):
    return HttpResponse('You are in gallery')
