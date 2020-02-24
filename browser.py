from xlutils.copy import copy
from xlrd import open_workbook
import calendar
from datetime import date
# https://www.stavros.io/posts/standalone-django-scripts-definitive-guide/
import os, sys

proj_path = "."
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learninglab.settings.production")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from accounts.models import Student
from votes.models import Response, Question
from grade.models import AttendanceInstance


# User input for class information

filename = "student_group.xls"

# prepare Excel file for reading
xl_workbook = open_workbook(filename)
xl_sheet = xl_workbook.sheet_by_index(0)
# prepare Excel file for writing
book = copy(xl_workbook)
sheet1 = book.get_sheet(0)

student_all = Student.objects.all()

response_all = Response.objects.all()

student_list = []

student_responses = []


# response 를 구체화 해서 입력

# for student in student_all:
#     temp_list = []
#     temp_list.append(student.student_no)

#     temp_responses = list(response_all.filter(student = student))
#     for response in temp_responses:
#         temp2_list = []
#         temp2_list.append(response.question.title)  #1
#         temp2_list.append(response.vote1)           #2
#         temp2_list.append(response.vote2)           #3
#         temp_list.append(temp2_list)


#     student_responses.append(temp_list)

for student in student_all:
    temp_list = []
    temp_list.append(student.section.section_no)
    temp_list.append(student.student_no)
    temp_list.append(student.name)
    temp_list.append(student.major)

    #response_list = [p for p in range(len(response_all)) if response_all[p].student == student]
    response_list = (response_all.filter(student = student))

    # temp_list.append(response_list)
    # print(response_list)

    normalized_score = 0.0
    score = 0.0
    prior_knowledge = False

    for response in response_list:
        if response.question.title == "coordinates of rigid body in 3d":

            if response.vote1 == 1:
                score += 0
            if response.vote1 == 2:
                score += 0
            if response.vote1 == 3:
                score += 0
            if response.vote1 == 4:
                score += 0

        if response.question.title == "Solvability of Ax=b":

            if response.vote1 == 1:
                score += 1
            if response.vote1 == 2:
                score += 3
                prior_knowledge = True
            if response.vote1 == 3:
                score += 2
            if response.vote1 == 4:
                score += 0

        if response.question.title == "Gauss Elimination - singular":

            if response.vote1 == 1:
                score += 0
            if response.vote1 == 2:
                score += 3
            if response.vote1 == 3:
                score += 1
            if response.vote1 == 4:
                score += 2

        if response.question.title == "Review for solvability":

            if response.vote1 == 1:
                score += 2
            if response.vote1 == 2:
                score += 0
            if response.vote1 == 3:
                score += 1
            if response.vote1 == 4:
                score += 3

        if response.question.title == "Inverse matrices by inspection":

            if response.vote1 == 1:
                score += 0
            if response.vote1 == 2:
                score += 0
            if response.vote1 == 3:
                score += 2
            if response.vote1 == 4:
                score += 0

        if response.question.title == "Calculation of LU":
            pass

        if response.question.title == "Review of LU, multiplication, & inverse":
            pass
    # end for

    temp_list.append(score)

    if response_list.count() != 0:
        temp_list.append(round(score/response_list.count(),2))
    else:
        temp_list.append(0)

    temp_list.append(prior_knowledge)
    print(temp_list)

    student_list.append(temp_list)


    # endfor student_list

for row in range(len(student_list)):
    for col in range(len(student_list[0])):
        sheet1.write(row+1,col, str(student_list[row][col]))




#sheet1.write(i, cols, 'x')



# student_in_each_class = ar.filter(datestamp=class_date,
#      student__section__section_no=section_number)                    

 
# sheet1.write(0,0,'x')
book.save(filename)
