from django.shortcuts import render
from django.http import HttpResponse
from . models import stud
from . models import society


def index(request):
    return HttpResponse("you have reached school")


def home(request):
    return HttpResponse("i am Aditya")


def college(request):
    return HttpResponse('i study in IGIT sarang')


def locha(request):
    students = stud.objects.all()  # fetches info from db
    context = {"students": students}
    return render(request, "index.html", context)


def bacha(request):
    information = stud.objects.all()
    context = {"information": information}
    return render(request, "index_2.html", context)


def mycomp(request):
    info = stud.objects.all()
    context = {"info": info}
    return render(request, "index_3.html", context)\



def details(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        Branch = request.POST.get("Branch")
        sem = request.POST.get("sem")
        print(name, roll, Branch, sem)
        s = stud(naam=name, roll=int(roll), Branch=Branch, sem=int(sem))
        try:
            s.save()
        except:
            return HttpResponse("Roll no. exists")
        return HttpResponse("Your form has been submitted")
    else:
        return render(request, "create.html")
