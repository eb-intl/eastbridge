from django.conf.urls import url

from .views import ClientDetail, ClientList


urlpatterns = [
    url(r'^(?P<slug>[-\w]+)$', ClientDetail.as_view(), name='detail'),
    url(r'^$', ClientList.as_view(), name='list'),
]
