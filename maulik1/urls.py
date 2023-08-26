from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.index, name='home'),
    path('abouteme/',views.abouteme,name='abouteme'),
    path('index/',views.index,name='index'),
#    path('contact',views.contact,name='contact'),
    
    ]
