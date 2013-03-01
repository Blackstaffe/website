from django.http import HttpResponse
from django.template import Context, loader

from showmanager.models import Show, Host
# Create your views here.
# these should be moved into seperate files for sanities sake
def index(request):
    # add a list of latest logs
    # add ability to find by time
    return HttpResponse("Some things would go here")

def genre(request):
    genrelist = Show.objects.order_by('genre')
    template = loader.get_template('archive/genre.html')
    context = Context({
        'genrelist': genrelist,
    })
    return HttpResponse(template.render(context))

def genre_detail(request):
    genre_info = Show.objects.filter('genre')
    template = loader.get_template('archve/genre_detail.html')
    context = Context({
        'showsingenre': showsingenre,
    })
    return HttpResponse(template.render(context))

def show_detail(request, show_id):
    show_info = Show.objects.get(pk=show_id)
    template = loader.get_template('archive/show_detail.html')
    context = Context({
        'show_info': show_info,
    })
    return HttpResponse(template.render(context))

def shows(request):
    latest_logs = Show.objects.order_by('timeslot')[:12] #this will break when the db model is updated
    template = loader.get_template('archive/shows.html')
    context = Context({
        'latest_logs': latest_logs,
    })
    return HttpResponse(template.render(context))

def hosts(request):
    host_list = Host.objects.order_by('host')
    template = loader.get_template('archive/hosts.html')
    context = Context({
        'host_list': host_list,
    })
    return HttpResponse(template.render(context))

def host_detail(request, host_id):
    hosts = Host.objects.get(pk=host_id)
    template = loader.get_template('archive/host_detail.html')
    context = Context({
        'hosts': hosts,
    })
    return HttpResponse(template.render(context))
