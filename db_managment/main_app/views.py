from django.shortcuts import render
from django.contrib import messages
from .models import Student, Course, Stacks
# Create your views here.

# Django ORM


# def testView(request):
#     # your db managment is here

#     # first_stack = Stacks.objects.first()
#     # last_stack = Stacks.objects.last()

#     # print(first_stack)
#     # print(last_stack)

#     # one_item = Course.objects.get(id=1)  # faqat 1 ta object olish
#     # print(one_item)

#     object_list = Student.object.filter()
#     # print(object_list)
#     data = {
#         "object": None
#     }
#     return render(request, "index.html",context=data)


# def search(request):
#     # print(request)
#     # return render(request, "index.html")
#     # print(request)
#     # print(request.path) # search
#     # print(request.get_full_path) #/seacrh/
#     # print(request.get_host())# 127.0.0.1:8000
#     # print(request.get_port()) # 8000
#     # print(request.method) #GET
#     # print(request.GET.get('q')) # input value
#     # print(request.GET['q'] # input value

#     # return render(request,"index.html")
#     if request.method == "GET":


#         query = request.GET.get("q")

#         data = Srudent.objects.filter(name_icontains=query)
#         if data:
#             return render(request, "index.html",
#                           context={"object_list":data})
#         else:
#             return render(request, "index.html",
#                           context={"object_list":'Result not found'})


#     return render(request, "index.html")


def testView(request):
    # your db managment is here

    # first_stack = Stacks.objects.first()
    # last_stack = Stacks.objects.last()

    # print(first_stack)
    # print(last_stack)
    # data = {
    #     "object":None
    # }

    # one_item = Course.objects.get(id=1)
    # print(one_item)
    #  = Course.objects.all()

    # object_list = Student.objects.filter()
    # print(object_list)
    course = Course.objects.all()
    data = {
        # 'object':None,
        "stacks": stacks,
        "courses": course
    }

    return render(request, "index.html", context=data)

    # if request.method == 'POST':


def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        data = Student.objects.filter(name__icontains=query)
        # data = Student.objects.filter(age_lt=int(query)) # lt - dan kichik
        # data = Student.objects.filter(age_lte=int(query)) # - lte ga teng yoki kichik
        # data = Student.objects.filter(age_gt=int(query)) # - dan katta
        # data = Student.objects.filter(age_gte=int(query)) # - gte ga teng yoki katta
        if data:
            return render(request, 'index.html', context={'object_list': data})
        else:
            return render(request, 'index.html', context={"message": "not found"})
        
        
        
        
def add_course_virew(request):
    if request.method == 'POST'
    name = request.POST.get("name")
    if len(name) < 3:
        
