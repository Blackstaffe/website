from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hiya I'm a test")

def show_detail(request, show_id):
    return HttpResponse("Show %s" % show_id)

def shows(request):
    return HttpResponse("This is where a list of shows would go")
