from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('secretaries/',views.secretaries,name = 'secretaries'),
    path('core/',views.core,name = 'core'),
    path('exec/',views.exec,name = 'exec'),
    path('gallery/',views.gallery,name = 'gallery'),
]
