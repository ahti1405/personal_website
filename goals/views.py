from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

from .models import Goal


class HomePageView(TemplateView):
    template_name = 'index.html'


class GoalsView(ListView):
    model = Goal
    context_object_name = 'goals'


class GoalDetailView(DetailView):
    model = Goal


class GoalCreateView(CreateView):
    model = Goal
    fields = '__all__'
    success_url = reverse_lazy('goal_list')


class GoalUpdateView(UpdateView):
    model = Goal
    fields = '__all__'
    success_url = reverse_lazy('goal_list')


class GoalDeleteView(DeleteView):
    model = Goal
    success_url = reverse_lazy('goal_list')
