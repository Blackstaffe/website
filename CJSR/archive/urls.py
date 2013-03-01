from django.conf.urls import patterns, url

from archive import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^shows/$', views.shows),
    # Url Scheme for show page
    url(r'^shows/(?P<show_id>\d+)/$', 
    views.show_detail, 
    name='show_detail'),
    # Url scheme for genre pages
    url(r'^genre/$', 
    views.genre, 
    name='genre'),
#    url(r^/genre/
     # maybe genre's should be referenced by an ID instead of a string would 
     # make this easier
    url(r'^hosts/$', 
    views.hosts, 
    name='hosts'),
    url(r'^hosts/(?P<host_id>\d+)/$', 
    views.host_detail, 
    name='host_detail'),
#    url(r'^/timeslot/', include(logmachine.views.timeslot)),
)
