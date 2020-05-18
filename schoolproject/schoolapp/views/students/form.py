from django.shortcuts import render, redirect, reverse
from schoolapp.models import Student

def get_student(student_id): 
    return Student.objects.get(pk=student_id)

def student_form(request):
    template = "students/form.html"
    context = {
    } 
    return render(request, template, context)

def student_edit_form(request, student_id): 
    student = get_student(student_id)
    template = "students/form.html"
    context= {
        'student': student
    }
    return render(request, template, context)