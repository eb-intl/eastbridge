from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleList(ListView):
    model = Article
    paginate_by = 10
    #queryset = Article.objects.filter(publish=True).order_by('-created')


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArticleList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books



        context['latest_news'] = Article.objects.all()[:3]

        return context

class ArticleDetail(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books



        context['latest_news'] = Article.objects.all()[:3]

        return context