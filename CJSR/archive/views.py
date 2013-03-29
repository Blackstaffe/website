from django.shortcuts import render
from django.template import Context, loader
from django.template import RequestContext
from showmanager.models import Show, Host
# Create your views here.
# these should be moved into seperate files for sanities sake
def index(request):
    #Time Lookup code
    latestlogs = Show.objects.order_by('timeslot')[:12]
    context = {'latestlogs': latestlogs}
    return render(request, 'archive/index.html', context, 
    context_instance=RequestContext(request)) 
def timelookup(request):
    timerequest = request.POST['time']
    daterequest = request.POST['date']
    #timeslot = showinfo.timeslot.strftime('%H-%M-%S')
    #startdate = showinfo.startdate.strftime('%Y-%M-%d')
    # this is almost working I just need to split up the forms and make them
    # better then constructing a file will be easier
    logfile = '%s/CJSR_%s_%s.mp3' % (folder, daterequest, timerequest)
    print logfile
    # This should be a response redirect with an
    # added context  not a straight return render 
    context = {'logfile': logfile}
    return render(request, 'archive/index.html', context) 

# this is uneccesary kept here for memories sake
def genre(request):
    genrelist = Show.objects.order_by('genre')
    context = {'genrelist': genrelist}
    return render(request, 'archive/genres.html', context)

def show_detail(request, show_id):
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
