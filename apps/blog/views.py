from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Article, ArticleFile


class ArticleList(ListView):
    model = Article
    paginate_by = 9


class FileList(ListView):
    model = ArticleFile
    paginate_by = 9


class ArticleSearch(ListView):
    model = Article
    paginate_by = 9
    template_name = 'blog/article_search.html'
    #queryset = Article.objects.filter(publish=True).order_by('-created')


class ArticleDetail(DetailView):
    model = Article
