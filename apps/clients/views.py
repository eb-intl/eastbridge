from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Client


class ClientList(ListView):
    model = Client
    paginate_by = 10


class ClientDetail(DetailView):
    model = Client

