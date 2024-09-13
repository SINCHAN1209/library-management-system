from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import *

def home(request):
    return render(request, "home.html", context={"current_tab":"home"})

def readers_tab(request):
    if request.method=="GET":
        readers= reader.objects.all()
        return render(request, "readers.html", context={"current_tab": "readers", "readers":readers})
    else:
        query = request.POST['query']
        readers = reader.objects.raw("select * from lims_App_reader where reader_name like'%"+query+"%'")
        return render(request, "readers.html", context={"current_tab": "readers", "readers":readers, "query":query})
    


def shopping(request):
    return HttpResponse("welcome to shopping")

def books(request):
    return render(request,'books.html',context={"current_tab": "books"})

def save_student(request):
    student_name= request.POST['student_name']
    return render(request, "welcome.html", context={'student_name':student_name})

def save_reader(request):
    print(request)
    reader_item= reader(reference_id=request.POST['reader_ref_id'],
                       reader_name=request.POST['reader_name'],
                       reader_contact=request.POST['reader_contact'],
                       reader_address=request.POST['address'],
                       active=True)
    reader_item.save()
    return redirect('/readers')