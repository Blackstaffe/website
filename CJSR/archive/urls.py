from django.conf.urls import patterns, url

from archive import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^shows/$', views.shows),
    # Url Scheme for show page
    url(r'^shows/(?P<show_id>\d+)/$', 
    views.show_detail, 
    name='show_detail'),
#    url(r'^/genre/$', views.genre),
#    url(r'^/hosts', include(logmachine.views.hosts)),
#    url(r'^/hosts/name', include(logmachine.views.host)),
#    url(r'^/timeslot/', include(logmachine.views.timeslot)),
)
