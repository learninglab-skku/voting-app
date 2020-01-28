# onlineclasses/urls.py
from django.urls import path

from .views import *


app_name = 'onlineclasses'

urlpatterns = [
    path('', VideoListView.as_view(), name='list'),
    path('<int:pk>', VideoDetailView.as_view(), name='detail'),
    # path('create', CourseCreateView.as_view(), name='create'),
    # path('edit/<int:pk>', CourseUpdateView.as_view(), name='edit'),
    # path('delete/<int:pk>', CourseDeleteView.as_view(), name='delete'),
]
