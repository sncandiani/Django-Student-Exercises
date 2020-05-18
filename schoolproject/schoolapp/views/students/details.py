from django.shortcuts import render, redirect, reverse
from schoolapp.models import Student

def get_student(student_id): 
    return Student.objects.get(pk=student_id)

def student_details(request, student_id): 
    # Request needs .method!
    if request.method == "GET": 
        student = get_student(student_id)
        template = "students/details.html"
        context = {
            'student': student
        }
        return render(request, template, context)
    elif request.method == "POST": 
        form_data = request.POST
        if( 
            "actual_method" in form_data 
            and form_data["actual_method"] == "DELETE"
        ): 
            student_to_delete = get_student(student_id)
            student_to_delete.delete()
            return redirect(reverse('schoolapp:students'))
        elif(
            "actual_method" in form_data 
            and form_data["actual_method"] == "PUT"
        ): 
            student_to_edit = get_student(student_id)
            
            student_to_edit.first_name = form_data["first_name"]
            student_to_edit.last_name = form_data["last_name"]
            student_to_edit.slack_handle = form_data["slack_handle"]

            student_to_edit.save()

            return redirect(reverse('schoolapp:students'))
    