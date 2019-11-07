from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *


# Create your views here.

# for the members page -- /members/
def home(request):
    sec = Secretaries.objects.all()
    core = Core.objects.all()
    exec = Executive.objects.all()
    gal = gallery.objects.all()
    context = {
        'sec': sec,
        'header': 'Secretaries',
        'core': core,
        'header': 'Core',
        'exec': exec,
        'header': 'Executives',
        'gal': gal,
        'header': 'Gallery',
    }
    return render(request, 'members/main.html',context)
