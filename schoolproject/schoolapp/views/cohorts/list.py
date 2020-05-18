from django.shortcuts import render
from schoolapp.models import Cohort

def cohort_list(request): 
    all_cohorts = Cohort.objects.all()
    template = 'cohorts/list.html'
    context = {
        "cohorts": all_cohorts
    }
    return render(request, template, context)
