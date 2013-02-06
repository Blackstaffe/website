from django.contrib import admin
from showmanager.models import Show, Host
from django.contrib.admin import SimpleListFilter
class DayListFilter(SimpleListFilter):
    title = ('Day')
    parameter_name = 'day'
    
class TimeListFilter(SimpleListFilter):
    title = ('TimeSlot')
    parameter_name = 'starttime'

class HostInline(admin.StackedInline):
    model = Host
    extra = 1

class ShowAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basics', {'fields': ['name', 'day', 'starttime', 'tagline', 'description',]}), 
        ('Contact Info', {'fields': ['website', 'email', 'twitter', 'facebook']}),
    ]
    inlines = [HostInline]
    list_display = ('name', 'day', 'starttime')
#   list_filter = (DayListFilter, TimeListFilter)
    search_fields = ['name', 'host',] 
admin.site.register(Show, ShowAdmin)
