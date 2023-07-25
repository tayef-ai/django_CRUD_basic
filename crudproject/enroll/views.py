from django.shortcuts import render, HttpResponsePermanentRedirect
from .forms import StudentRegistration
from .models import Student
from django.core import validators
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name = nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'enroll/addandshow.html', {'fm': fm, 'st': stud})


def delete_data(request, id):
    if request.method == 'POST':
        dt = Student.objects.get(pk=id)
        dt.delete()
        return HttpResponsePermanentRedirect('/')
    
def edit_data(request, id):
    if request.method == 'POST':
        dt = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=dt)
        if fm.is_valid():
            fm.save()
            return HttpResponsePermanentRedirect('/')
    else:
        dt = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=dt)
    return render(request, 'enroll/updatestudent.html', {'fm': fm})    
