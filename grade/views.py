# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator

# from .resources import StudentResource
from learninglab.decorators import student_required, teacher_required

from django.conf import settings # 추천!

from accounts.models import Student, User
from grade.models import Grade, AttendanceInstance
from datetime import date
import calendar
from votes.models import Response
# Create your views here.

## 학생 정보 페이지.
@method_decorator(student_required, name='dispatch')
class Student_MyPage(View):
    def get(self, request):

        ### Parse user_id
        user_id = request.user.get_username() #eirc8260


        ### Get the user Info 
        Info = self.get_student_info(user_id)


        ### Get the User Score Info
        # score_info = Grade.objects.get(student=Info.pk)


        ### Get Student Attendance
        # double vote error
        fall = range(9,13)
        spring = range(3,7)
        season = Info.section.course.semester
        if season == 'Fall':
            semester = fall
        if season == 'Spring':
            semester = spring


        YEAR = Info.section.course.year
        classes = ['TUESDAY', 'THURSDAY']


       
        #student_number = Student.objects.get(user = request.user.id).student_no

        #student_number = request.user.Student.student_no
        # print("==================\n",request.user.pk)
        # print("==================\n",request.user.username)
        attendance_all = AttendanceInstance.objects.all()
        student_number = Student.objects.get(user__id = request.user.id).student_no

        attendance_list = []
        for month in semester:
                mycal = calendar.monthcalendar(YEAR, month)
                for week in mycal:
                    for each in classes:
                        temp_instance = []                  # list that contains current date & at
                        if week[getattr(calendar, each)]:

                            temp_instance.append(date(YEAR, month, week[getattr(calendar, each)]))#lecture_date


                            class_date = date(YEAR, month, week[getattr(calendar, each)])
                            student_attendance = attendance_all.filter(datestamp=class_date,
                                                     student__student_no=student_number)
                            if student_attendance:
                                temp_instance.append(1)
                            else:
                                temp_instance.append(0)         # 0 for absense, 1 for attending
                            attendance_list.append(temp_instance)
        

        ### Response
        return render(request, 'accounts/student_mypage.html', {'Info': Info, 'attendance_list':attendance_list})
        ### Commented out by Jun 9/4/19 due to multiple grade instances: remove score_info.
        # return render(request, 'accounts/student_mypage.html', {'Info': Info, 'score_info':score_info,
        #                 'attendance_list':attendance_list})

    #TODO: 
    def get_student_info(self, user_id):
        std_list = Student.objects.all()
        for n in std_list:
            if n.get_username() == user_id:
                return n
                break
        return None