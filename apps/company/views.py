from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Employee


class EmployeeList(ListView):
    model = Employee
    paginate_by = 8


class EmployeeDetail(DetailView):
    model = Employee

