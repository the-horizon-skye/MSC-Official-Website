from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *


# Create your views here.

# for the members page -- /members/
def home(request):
    return HttpResponse("You are in The Home Page of Members")

def secretaries(request):
    sec = Secretaries.objects.all()
    context = {
        'sec': sec,
        'header': 'Secretaries',
    }
    return render(request,'members/secretaries.html',context)
def core(request):
    core = Core.objects.all()
    context = {
        'core': core,
        'header': 'Core',
    }
    return render(request,'members/core.html',context)

def exec(request):
    exec = Executive.objects.all()
    context = {
        'exec': exec,
        'header': 'Executives',
    }
    return render(request,'members/exec.html',context)


# for the gallery in members -- /members/gallery/
def gallery(request):
    return HttpResponse('You are in gallery')
