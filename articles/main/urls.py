from django.urls import path 
from .import views 

app_name = 'main'

urlpatterns = [
    path("", views.homePageView, name='home'),
    path("contact/", views.qurutsPageView, name='contact'),
]
