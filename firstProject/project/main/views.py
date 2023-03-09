from django.shortcuts import render

# Create your views here.


def homePageView(request):
    return render(request, 'index.html')

def aboutPageView(request):
    return render(request, 'about.html')

def contactPageView(request):
    return render(request, 'contact.html')