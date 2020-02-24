# courses/urls.py
from django.urls import path

from .views import (
    CourseListView, CourseDetailView, CourseCreateView,
    CourseUpdateView, CourseDeleteView, LectureListView
)


app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('<int:pk>', CourseDetailView.as_view(), name='detail'),
    path('<int:course_pk>/list', LectureListView.as_view(), name='lecture_list'),
    path('create', CourseCreateView.as_view(), name='create'),
    path('edit/<int:pk>', CourseUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', CourseDeleteView.as_view(), name='delete'),
]
