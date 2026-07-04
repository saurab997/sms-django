from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render (request, 'index.html', context)
    
def delete(request, id):
    student = Student.objects.get(id = id)
    student.delete()
    return redirect('/')

def create(request):
    name = request.POST.get('name')
    roll = request.POST.get('roll')
    age = request.POST.get('age')
    Class = request.POST.get('Class')

    Student.objects.create(
        name = name,
        roll = roll,
        age = age,
        Class = Class
    )

    return redirect('/')

def update(request, id):
    student = Student.objects.get(id = id)
    student.name = request.POST.get('name')
    student.roll = request.POST.get('roll')
    student.age = request.POST.get('age')
    student.Class = request.POST.get('Class')
    student.save()
    
    return redirect('/')