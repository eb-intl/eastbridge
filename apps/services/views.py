#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import ServiceGroup, Service


class ServiceListView(generic.ListView):
    model = ServiceGroup



class ServiceDetailView(generic.DetailView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['all_services'] = Service.objects.all()
        return context