# courses/urls.py
from django.urls import path

from .views import *


app_name = 'homework'

urlpatterns = [
    path('', HomeworkListView.as_view(), name='homework_list'),
    path('detail/<int:no>', HomeworkDetailView, name='homework_detail'),
    path('api/v1/start', HomeworkStartView.as_view(), name='hw_start'),
    path('api/v1/end', HomeworkEndView.as_view(), name='hw_end'),
    path('api/v1/homework/list/<int:hw_no>', HomeworkAllList, name='hw_all_list'),
    path('api/v1/homework/check/<int:course_id>/<int:hw_no>', HomeworkCheckList, name='hw_all_list'),
    path('tracker', HomeworkTrackerView.as_view(), name='homework_tracker'),


    # path('api/v1/viedo/one/start', HomeworkEndView.as_view(), name='hw_end'),
    # path('api/v1/viedo/two/start', HomeworkEndView.as_view(), name='hw_end'),
]
