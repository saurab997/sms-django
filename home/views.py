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
    if request.method == "POST": #if request is post then only perform the delete operation 
        student.delete()
    return redirect('home')

def create(request):
    if request.method == "GET":
        return render(request, "create.html")
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

    return redirect('home') #if this is not done and again render then it goes to loop type, security threat

def update(request, id):
    if request.method == "GET":
        student = Student.objects.get(id = id)
        context={
            'student' : student
        }
        return render(request, "update.html", context)
    student = Student.objects.get(id = id)
    student.name = request.POST.get('name')
    student.roll = request.POST.get('roll')
    student.age = request.POST.get('age')
    student.Class = request.POST.get('Class')
    student.save()
    
    return redirect('home')