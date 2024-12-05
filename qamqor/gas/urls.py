from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about', views.about, name='about'),
    path('appraisals', views.appraisals, name='appraisals'),
    path('brokerage', views.brokerage, name='brokerage'),
    path('consulting', views.consulting, name='consulting'),
    path('contact', views.contact, name='contact'),
]