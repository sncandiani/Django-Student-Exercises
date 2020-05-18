from django.shortcuts import render
from schoolapp.models import Exercise

def exercise_list(request): 
    all_exercises= Exercise.objects.all()
    template = 'exercises/list.html'
    context = {
        "exercises": all_exercises
    }
    return render(request, template, context)
