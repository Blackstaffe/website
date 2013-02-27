from django.http import HttpResponse
from django.template import Context, loader

from showmanager.models import Show, Host
# Create your views here.
def index(request):
    return HttpResponse("Some things would go here")

def show_detail(request, show_id):
    return HttpResponse("This is where details about a show would go")

def shows(request):
    latest_logs = Show.objects.order_by('timeslot')[:12] #this will break when the db model is updated
    template = loader.get_template('archive/index.html')
    context = Context({
        'latest_logs': latest_logs,
    })
    return HttpResponse(template.render(context))
