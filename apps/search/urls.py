from django.conf.urls import url

from .views import ArticleList, ArticleDetail


urlpatterns = [
    url(r'^$', ArticleList.as_view(), name='search'),
]
