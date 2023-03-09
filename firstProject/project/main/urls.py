from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('about/', views.aboutPageView, name='about'),
    path('contact/', views.contactPageView, name='contact')
]