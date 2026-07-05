from django.shortcuts import render,redirect, get_object_or_404
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    response = render (request, 'index.html', context)
    response.set_cookie('visited', 'True')
    return response
    
def delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST": #if request is post then only perform the delete operation 
        student.delete()
    return redirect('home')

from django.http import HttpResponse
def create(request):
    if not request.COOKIES.get("visited") == "True":
        return HttpResponse("Please go through the process from homepage")
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
        student = get_object_or_404(Student, id=id)
        context={
            'student' : student
        }
        return render(request, "update.html", context)
    student = get_object_or_404(Student, id=id)
    student.name = request.POST.get('name')
    student.roll = request.POST.get('roll')
    student.age = request.POST.get('age')
    student.Class = request.POST.get('Class')
    student.save()
    
    return redirect('home')