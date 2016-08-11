from django.conf.urls import url

from .views import ProductDetail, ProductList

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)$', ProductDetail.as_view(), name='detail'),
    url(r'^$', ProductList.as_view(), name='list'),
]
