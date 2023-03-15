from django.shortcuts import render

# Create your views here.

from .models import Category, Product
def homePageView(request):
    product = Product.objects.all()
    category = Category.objects.all()
    data = {
        'prducts':products,
        'categories':categories
    }
    return render(request, 'index.html',context=data)

def qurutPageView(request):
    return render(request,'quruts.html')
# def homePageView(request):
#     return render(request, 'index.html')

# def aboutPageView(request):
#     return render(request, 'about.html')

# def contactPageView(request):
#     return render(request, 'contact.html')
