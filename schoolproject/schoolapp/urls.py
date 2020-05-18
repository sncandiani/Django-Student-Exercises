from django.urls import path
from .views import *

app_name = "schoolapp"

urlpatterns = [
    path('', student_list, name='home'),
    path('students/', student_list, name='students'),
    path('students/form', student_form, name='student_form'),
    path('student/<int:student_id>', student_details, name='student_details'),
    path('student/<int:student_id>/form/', student_edit_form, name='student_edit_form'),
    path('instructors/', instructor_list, name='instructors'), 
    path('exercises/', exercise_list, name='exercises'),
    path('cohorts/', cohort_list, name='cohorts')
]