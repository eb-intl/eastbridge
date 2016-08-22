from django.views.generic import ListView, DetailView

from .models import Tag


class TagList(ListView):
    model = Tag
    paginate_by = 9


class TagDetail(DetailView):
    model = Tag
