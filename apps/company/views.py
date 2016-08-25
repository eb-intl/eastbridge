from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
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


def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
