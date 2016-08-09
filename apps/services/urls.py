from django.conf.urls import url, include, patterns

from .views import ServiceListView, ServiceDetailView


urlpatterns = patterns('',
    url(r'^$', ServiceListView.as_view(), name='list'),
    url(r'^(?P<slug>[-\w]+)/$', ServiceDetailView.as_view(), name='detail'),

    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)