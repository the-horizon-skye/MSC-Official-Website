from django.shortcuts import render

#makeathon
def home(request):
    return render(request,'makeathon/index.html')

# Create your views here.
