from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

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


class LatestEntriesFeed(Feed):
    title = "EastBridge Strategic Sourcing - News"
    link = "/news/"
    description = "Latest news from EastBridge Strategic Sourcing"

    def items(self):
        return Article.objects.order_by('-created')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

