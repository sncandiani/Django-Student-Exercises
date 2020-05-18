import sqlite3
from django.shortcuts import render, redirect, reverse
from schoolapp.models import Student
from ..connection import Connection

def student_list(request): 
    if request.method=="GET":
        # !!!!!!!!
        # Using ORM 
        all_students = Student.objects.all()
        # !!!!!!!!
        # Using SQL queries 

        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     SELECT
	    #         s.id, 
	    #         s.first_name, 
	    #         s.last_name, 
	    #         s.slack_handle, 
	    #         s.cohort_id
        #         FROM schoolapp_student s      
        #     """)

        #     all_students = []
        #     dataset = db_cursor.fetchall()

        #     # make into rows 
        #     for row in dataset: 
        #         student = Student()
        #         student.first_name = row["first_name"]
        #         student.last_name = row["last_name"]
        #         student.slack_handle = row["slack_handle"]
        #         student.cohort_id = row["cohort_id"]
        #         all_students.append(student)
        template = 'students/list.html'
        context = {
            'students': all_students
        }
        return render(request, template, context)
    elif request.method=="POST": 
        form_data = request.POST
        new_student = Student()
        new_student.first_name = form_data['first_name']
        new_student.last_name = form_data['last_name']
        new_student.slack_handle = form_data['slack_handle']
        
        new_student.save()

        return redirect(reverse('schoolapp:students'))