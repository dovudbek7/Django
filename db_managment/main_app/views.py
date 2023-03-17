from django.shortcuts import render
from .models import Student, Course, Stacks
# Create your views here.

# Django ORM


def testView(request):
    # your db managment is here

    # first_stack = Stacks.objects.first()
    # last_stack = Stacks.objects.last()

    # print(first_stack)
    # print(last_stack)

    # one_item = Course.objects.get(id=1)  # faqat 1 ta object olish
    # print(one_item)
    
    # object_list = Student.object.filter(name_exact='Nazrulloh')
    # print(object_list)
    data = {
        "object": None
    }
    return render(request, "index.html", context=data)



def search(request):
    # print(request)
    # return render(request, "index.html")
    # print(request)
    # print(request.path) # search
    # print(request.get_full_path) #/seacrh/
    # print(request.get_host())# 127.0.0.1:8000
    # print(request.get_port()) # 8000
    # print(request.method) #GET
    print(request.GET.get('q')) # input value
    print(request.GET['q'] # input value
    return render(request,"index.html")


