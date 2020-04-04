import os, sys
import csv

proj_path = "/home/jun/learninglab"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learninglab.settings.production")
sys.path.append(proj_path)

###########################
# # for 2019 summer project
# proj_path = "/Users/Bambiz/Dev/git/voting-app-new/voting-app/"
# # This is so Django knows where to find stuff.
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learninglab.settings.local")
# sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from accounts.models import Student, Major
from courses.models import Section, Group

User = get_user_model()

### group or user? ###
switch = 3

### Course Info ###
year = 2020
# title = "E"
title = "Engineering Mathematics 1"

if switch == 1:
    #########################
    ##### create groups #####
    #########################
    """
    Sections are already created manually using admin mode

    """
    class_no = [41, 42, 43, 44]
    number_of_groups = [13, 14, 15, 17]

    # section = models.Section.objects.get(section_no=41, course__year=year, course__title=title)
    # models.Group.objects.create(section=section, group_no=2)

    for number in class_no:
        section = Section.objects.get(section_no=number, course__year=year, course__title=title)
        for g_number in range(number_of_groups[class_no.index(number)]):
            Group.objects.create(section=section, group_no=g_number + 1)

if switch == 2:
    #########################
    ##### create majors #####
    #########################
    with open("./em1_major.csv",encoding = 'UTF8') as f:
        majors = []
        for line in csv.reader(f):
            line = "".join(line)
            majors.append(line)

    for major in majors:
        Major.objects.create(title=major)

if switch == 3:
    #################################
    ##### create user instances ######
    #################################
    # import users from csv file
    with open("./em1_student.csv", encoding = 'UTF8') as f:
        users = [tuple(line) for line in csv.reader(f)]
    # print(users)



    ### check for existing, deleted or modified students.
    student_all = Student.objects.all()
    txtf = open("./students_to_delete.txt",'w')

    # if students delete course, show them on a txt file
    for student in student_all:
        exist_flag = 0
        for username, password, student_no, name, major, section, group, is_leader in users:
            if student.get_username() == username:
                exist_flag = 1
        if exist_flag == 0:
            txtf.write(str(student.student_no) + '\t' + student.name + '\t' + student.get_username() + '\n')
            print("students to delete : " + str(student.student_no) + '\t' + student.name + '\t' + student.get_username())

    txtf.close()





    # create users
    for username, password, student_no, name, major, section, group, is_leader in users:


        if username == "" :      # End of File. break.
            break

        # if student exist, skip.
        # if student is modified, apply changes in section.
        no_insert_flag = 0
        for student in student_all:
            if student.get_username() == username:
                no_insert_flag = 1       # don't create user.         

                if (student.section.section_no != int(section)) or (student.group.group_no != int(group)):
                    student.section = Section.objects.get(section_no=section, course__year=year, course__title=title)
                    student.group = Group.objects.get(section__section_no=section, section__course__year=year, section__course__title=title, group_no=group)
                    student.save()
                    print(student.name + " is successfully modified")
                else:
                    print(student.name + " has no change")


        if no_insert_flag == 1:    # skips to next.
            continue

        try:
            print('Creating user {0}.'.format(username))
            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.is_student=True
            user.save()

            assert authenticate(username=username, password=password)
            print('User {0} successfully created.'.format(username))

            # create student - onetoneField with user
            student = Student(user=user)

            student.student_no = student_no
            student.name = name
            student.major = Major.objects.get(title=major)
            student.section = Section.objects.get(section_no=section, course__year=year, course__title=title)
            student.group = Group.objects.get(section__section_no=section, section__course__year=year, section__course__title=title, group_no=group)
            student.is_leader = is_leader
            student.save()

        except:
            print('There was a problem creating the user: {0}.  Error: {1}.' \
                .format(username, sys.exc_info()[1]))
