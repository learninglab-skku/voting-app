# onlineclasses/views.py

from django.shortcuts import render

# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView, CreateView, UpdateView, View, DetailView
)
from django.core.exceptions import ObjectDoesNotExist
# from django.views.generic.edit import FormMixin
# import datetime
from django.utils import timezone
import pytz
# from django.db.models import Count, Q

from .models import *
from accounts.models import Student
from courses.models import Section
from learninglab.decorators import student_required, teacher_required
# from .forms import VoteForm

from grade.models import AttendanceInstance
import datetime



# Create your views here.

@method_decorator(student_required, name='dispatch')
class VideoDetailView(View):
    # model = Question
    def get(self, request, *args, **kwargs):
        video = Video.objects.get(pk = kwargs["pk"])


        return render(request,
            "onlineclasses/video_detail.html",
            {"video": video, })


    # def post(self, request, *args, **kwargs):
    #     question = get_object_or_404(Question, pk=kwargs["pk"])
    #     if "_check_vote" in self.request.POST:
    #         print("Check Vote")
    #         question.is_active = True
    #         question.code = 1
    #         question.save()
    #     elif "_vote_again" in self.request.POST:
    #         print("Vote Again")
    #         question.code = 2
    #         question.save()
    #     elif "_plot" in self.request.POST:
    #         print("Plot")
    #         return redirect("votes:plot", pk=kwargs["pk"])
    #     elif "_list" in self.request.POST:
    #         print("list")
    #         # reset all parameters to zero
    #         # then go to QuestionListView
    #         qs = Question.objects.all()
    #         qs.update(is_active=False)
    #         qs.update(code=0)
    #         return HttpResponseRedirect(reverse("votes:list"))
    #    # elif "_status" in self.request.POST:
    #    # print("Get Status")
    #    #     return redirect("votes:status", pk=kwargs["pk"])
    #     return redirect("votes:detail", pk=kwargs["pk"], se=kwargs["se"])

class VideoListView(ListView):
    model = Video