from django.conf.urls import patterns, url

from archive import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
#    url(r'^archive/shows', views.shows),
#    url(r'^archive/shows/showID', include(logmachine.views.show)),
#    url(r'^archive/genre', include(logmachine.views.genre)),
#    url(r'^archive/hosts', include(logmachine.views.hosts)),
#    url(r'^archive/hosts/name', include(logmachine.views.host)),
#    url(r'^archive/timeslot/', include(logmachine.views.timeslot)),
)
