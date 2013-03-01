from django.contrib import admin
from showmanager.models import Show, Host, Genre
from django.contrib.admin import SimpleListFilter

"""
class DayListFilter(SimpleListFilter):
    title = ('Day')
    parameter_name = 'day'
class TimeListFilter(SimpleListFilter):
    title = ('Time Slot')
    parameter_name = 'starttime'
"""
class HostInline(admin.StackedInline):
    model = Host
    extra = 1
class GenreInline(admin.StackedInline):
    model = Genre
class GenreAdmin(admin.ModelAdmin):
    model = Genre
    # The model needs to be updated to make genre's addable
class ShowAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basics', {'fields': ['name', 'slug', 'day', 'startdate', 'biweekly', 'timeslot', 'length', 
         'description', 'inactive']}),
        ('Contact Info', {'fields': ['website', 'email', 'twitter', 'facebook']}),
    ]
    inlines = [HostInline, GenreInline,]
    list_display = ('name', 'day', 'timeslot')
    list_filter = ['timeslot', 'day', 'genre']
    search_fields = ['name', 'host',] 
admin.site.register(Show, ShowAdmin,)
admin.site.register(Genre)
