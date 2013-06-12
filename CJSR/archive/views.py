from django.shortcuts import render
from django.template import Context, loader
from django.template import RequestContext
from archive.forms import TimeLookupForm
from showmanager.models import Show, Host, Genre
from datetime import datetime, timedelta
# Create your views here.
def index(request):
    latestlogs = []
    hour = 2
    hourstoday = int(datetime.now().strftime('%H')) - 1
    for i in range(0, hourstoday):
        logdatetime = datetime.now() - timedelta(hours=hour)
        latestlogs.append(logdatetime.strftime('%Y-%m/CJSR_%Y-%m-%d_%H-00-00.mp3'))
        hour += 1
    context = {'latestlogs': latestlogs,}
    return render(request, 'archive/index.html', context)
def timelookup(request):
    if request.method == 'POST':
        form = TimeLookupForm(request.POST)
        if form.is_valid():        
            print form
            return HttpResponseRedirect('/thanks/')
    
    else:
        form = TimeLookupForm()
        print form.media
    return render(request, 'archive/timelookup.html', {
         'form': form,
    })
def genres(request):
    genrelist = Genre.objects.all()
    context = {'genrelist': genrelist}
    return render(request, 'archive/genres.html', context)

def show_detail(request, show_id):
    showinfo = Show.objects.get(pk=show_id)
    latestlogs = []
    day = 0
    database_date = showinfo.timeslot_startdate
    print showinfo.timeslot_startdate
    database_weekday = database_date.weekday()
    loghour = database_date.hour
    print loghour
    now_date = datetime.now().replace(hour=loghour,
        minute=0, second=0, microsecond=0)
    now_weekday = now_date.weekday()
    diffrence_of_weekday = database_weekday - now_weekday
    if diffrence_of_weekday > 0:
        diffrence_of_weekday -= 7
        latest_show = now_date + timedelta(days=diffrence_of_weekday)
    else:
        latest_show = now_date + timedelta(days=diffrence_of_weekday)
    
    for i in range(0,9):
        logdatetime = latest_show - timedelta(days=day)
        print logdatetime
        latestlogs.append(logdatetime.strftime('%Y-%m/CJSR_%Y-%m-%d_%H-00-00.mp3'))
        day += 7
    context = {'latestlogs': latestlogs,
       'showinfo': showinfo}
    return render(request, 'archive/show_detail.html', context)

def shows(request):
    # Okay so this will nedd to be a dictionary to pass this usefully i can
    # generate the days of the week using the python datetime function
    weekday_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday']
    
    weekdays = []
    for i in range(0, 6):
        weekdays.append(Show.objects.filter(timeslot_startdate__week_day=i+1))
    print weekdays
    context = {'weekdays' : weekdays, 'weekday_names' : weekday_names}
    return render(request, 'archive/shows.html', context)
