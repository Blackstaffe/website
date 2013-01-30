from django.contrib import admin
from showmanager.models import Show, Hosts, Contact
from django.contrib.admin import SimpleListFilter
class DayListFilter(SimpleListFilter):
    title = ('Day')
    parameter_name = 'day'
    
class TimeListFilter(SimpleListFilter):
    title = ('TimeSlot')
    parameter_name = 'starttime'

class HostsInline(admin.StackedInline):
#    inlines = [ContactInline]
# Cannot stack menus inline, need to find work around (seperate hosts 
# interaction perhaps
    model = Hosts
    extra = 1
    
class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1

class ShowAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basics', {'fields': ['name', 'day', 'starttime', 'tagline', 'description',]}),
    ]
    inlines = [HostsInline]
    list_display = ('name', 'day', 'starttime')
#   list_filter = (DayListFilter, TimeListFilter)
    search_fields = ['name', 'hosts',] 
admin.site.register(Show, ShowAdmin)
