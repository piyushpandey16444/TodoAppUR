from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "task_list.html"


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "base/detail.html"


class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')
    template_name = "base/task_form.html"


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')
    template_name = "base/task_form.html"


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = "base/task_confirm_delete.html"
    success_url = reverse_lazy('task-list')
