from django.shortcuts import render
from schoolapp.models import Instructor

def instructor_list(request): 
    all_instructors = Instructor.objects.all()
    template = 'instructors/list.html'
    context = {
        "instructors": all_instructors
    }
    return render(request, template, context)
