from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from showmanager.models import Show, Host
# Create your views here.
# these should be moved into seperate files for sanities sake
def index(request):
    latestlogs = Show.objects.order_by('timeslot')[:12]
    context = {'latestlogs': latestlogs}
    return render(request, 'archive/index.html', context) 

# this is uneccesary kept here for memories sake
def genre(request):
    genrelist = Show.objects.order_by('genre')
    context = {'genrelist': genrelist}
    return render(request, 'archive/genre.html', context)

def genre_detail(request):
    genre_info = Show.objects.filter('genre')
    context = {'showsingenre': showsingenre}
    return render(request, 'archive/genre_detail.html', context)

def show_detail(request, show_id):
    showinfo = Show.objects.get(pk=show_id)
    context = {'showinfo': showinfo}
    return render(request, 'archive/show_detail.html', context)

# Change this to reference by absolute time value
def shows(request):
    sunday = Show.objects.filter(day__exact='Sunday')    
    monday = Show.objects.filter(day__exact='Monday')    
    tuesday = Show.objects.filter(day__exact='Tuesday')    
    wednesday = Show.objects.filter(day__exact='Wednesday')    
    thursday = Show.objects.filter(day__exact='Thursday')    
    friday = Show.objects.filter(day__exact='Friday')    
    saturday = Show.objects.filter(day__exact='Saturday')    
    context = {'sunday': sunday,
    'monday': monday,
    'tuesday': tuesday,
    'wednesday': wednesday,
    'thursday': thursday,
    'friday': friday,
    'saturday': saturday,}
    return render(request, 'archive/shows.html', context)

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
