from django.conf.urls import url

from views import OfficeDetail, OfficeList

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)$', OfficeDetail.as_view(), name='detail'),
    url(r'^$', OfficeList.as_view(), name='list'),
]
