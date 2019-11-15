from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse,HttpResponseRedirect
from .models import *


# Create your views here.

# for the members page -- /members/
def home(request):
    sec = Secretaries.objects.all()
    core = Core.objects.all()
    exec = Executive.objects.all()
    context = {
        'sec': sec,
        'header': 'Secretaries',
        'core': core,
        'header': 'Core',
        'exec': exec,
        'header': 'Executives',
    }
    return render(request, 'members/main.html',context)
def gall(request):
    gal = gallery.objects.all()
    paginator = Paginator(gal, 20)
    page = request.GET.get('page')
    gal = paginator.get_page(page)
    context = {
        'gal': gal,
        'header': 'Gallery',
    }
    return render(request, 'members/gallery.html',context)
