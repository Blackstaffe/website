from django.shortcuts import render
from django.template import Context, loader
from django.template import RequestContext
from showmanager.models import Show, Host
from datetime import datetime, timedelta
# Create your views here.
# these should be moved into seperate files for sanities sake
def index(request):
    latestlogs = []
    hour = 1
    for l in range(0,11):
        logdatetime = datetime.now() - timedelta(hours=hour)
        latestlogs.append(logdatetime.strftime('%Y_%m/CJSR_%Y-%m-%d_%H-00-00.mp3'))
        hour += 1
    context = {'latestlogs': latestlogs,}
    return render(request, 'archive/index.html', context)
def timelookup(request):
    # Check if a request has been made
    try:
        request.POST['logrequest']
    except (KeyError):
        context = {
        'daterange': range(1, 32),
        'hourrange' : range(0, 24),}
        return render(request, 'archive/timelookup.html', context)
    else:
        year = request.POST['year']
        month = "%02d" %(int(request.POST['month']),)
        day = "%02d" % (int(request.POST['date']),)
        hour = "%02d" % (int(request.POST['hour']),)
        logfile = '%s_%s/CJSR_%s-%s-%s_%s-00-00.mp3' % (
        year, month, year, month, day, hour)
        context = {'logfile' : logfile,
        'daterange': range(1, 32),
        # This should be a dictionary that references a list of numbers eg. '12am' : 0 
        'hourrange' : range(0, 24),}
        return render(request, 'archive/timelookup.html', context,
    context_instance=RequestContext(request))

# this is uneccesary kept here for memories sake
def genre_detail(request):
    genrelist = Show.objects.order_by('genre')
    context = {'genrelist': genrelist}
    return render(request, 'archive/genre_detail.html', context)

def show_detail(request, show_id):
    #timeslot = showinfo.timeslot.strftime('%H-%M-%S')
    #startdate = showinfo.startdate.strftime('%Y-%M-%d')
    # make a list of last 10 episodes 
    #CJSR_2013-03-25_23-00-00.mp3
    showinfo = Show.objects.get(pk=show_id)
    # This should be a function of the module because building a string for
    # the file name will be reused
    timeslot = showinfo.timeslot.strftime('%H-%M-%S')
    startdate = showinfo.startdate.strftime('%Y-%M-%d')
    logfile = 'CJSR_%s_%s.mp3' % (startdate, timeslot) 
    print logfile
    context = {'showinfo': showinfo}
    return render(request, 'archive/show_detail.html', context)

def shows(request):
    # make a list and use a for loop this is ugly 
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
