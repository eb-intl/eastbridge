from django.conf.urls import url

from .views import ArticleSearch, ArticleDetail, ArticleList, FileList


urlpatterns = [

    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)$',
        ArticleDetail.as_view(), name='detail'),

    url(r'^search$', ArticleSearch.as_view(), name='search'),
    url(r'^files$', FileList.as_view(), name='file_list'),

    url(r'^search$', ArticleSearch.as_view(), name='search'),
    url(r'^$', ArticleList.as_view(), name='list'),
]
