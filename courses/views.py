# courses/views.py
# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView, DeleteView
)

from . import mixins
from . import models
from learninglab.decorators import student_required, teacher_required


# @method_decorator(login_required, name='dispatch')
class CourseListView(ListView):
    model = models.Course


# @method_decorator(login_required, name='dispatch')
class CourseDetailView(DetailView):
    model = models.Course


@method_decorator(teacher_required, name='dispatch')
class CourseCreateView(
    LoginRequiredMixin, mixins.PageTitleMixin,
    mixins.SuccessMessageMixin, CreateView):
    fields = ('title', 'year', 'semester', 'goal', )
    model = models.Course
    page_title = "Create a Course."
    success_message = "Course created!"

    # Treehouse example
    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial["year"] = datetime.datetime.now().year
    #     # initial["coach"] = self.request.user
    #     return initial


@method_decorator(teacher_required, name='dispatch')
class CourseUpdateView(
    LoginRequiredMixin, mixins.PageTitleMixin,
    mixins.SuccessMessageMixin, UpdateView):
    fields = ('title', 'year', 'semester', 'goal', )
    model = models.Course

    def get_page_title(self):
        obj = self.get_object()
        return "Update {}".format(obj.title)

    def get_success_message(self):
        obj = self.get_object()
        return "{} updated!".format(obj.title)


@method_decorator(teacher_required, name='dispatch')
class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Course
    success_url = reverse_lazy("courses:list")

    # Treehouse example
    # def get_queryset(self):
    #     if not self.request.user.is_superuser:
    #         return self.model.objects.filter(user=self.request.user)
    #     return self.model.objects.all()
