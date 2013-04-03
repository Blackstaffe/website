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
#    url(r'^genres/$', 
#    views.genre, 
#    name='genres'),
    # URL Scheme for timelookup form submit
    url(r'^timelookup/$', 
    views.timelookup, 
    name='timelookup'),
#    url(r^/genre/
     # maybe genre's should be referenced by an ID instead of a string would 
     # make this easier -   url(r'^genres/(?P<genre_id>\d+)/$', 
#    url(r'^/timeslot/', include(logmachine.views.timeslot)),
)
