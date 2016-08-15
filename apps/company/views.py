from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Employee, Office


class EmployeeList(ListView):
    model = Employee
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(EmployeeList, self).get_context_data(**kwargs)
        context['executives'] = Employee.objects.filter(executive=True)
        context['others'] = Employee.objects.filter(executive=False)
        return context


class EmployeeDetail(DetailView):
    model = Employee


class OfficeList(ListView):
    model = Office
    paginate_by = 8


class OfficeDetail(DetailView):
    model = Office
