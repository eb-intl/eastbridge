from django.conf.urls import url, include

from views import EmployeeDetail, EmployeeList

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)$', EmployeeDetail.as_view(), name='detail'),
    url(r'^$', EmployeeList.as_view(), name='list'),
]
