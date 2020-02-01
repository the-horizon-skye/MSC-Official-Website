from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('index.urls',namespace='index'),name='index'),
    path('members/',include('members.urls',namespace='members'),name='members'),
    path('events/',include('events.urls', namespace='events'), name='events'),
    path('makeathon/',include('makeathon.urls', namespace='makeathon'), name='makeathon'),
]
