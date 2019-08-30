# courses/urls.py
from django.urls import path

from .views import (
    Student_MyPage
)


app_name = 'grade'

urlpatterns = [
    path('student_mypage', Student_MyPage.as_view(), name='student_mypage'),

]
