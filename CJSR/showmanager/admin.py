from django.contrib import admin
from showmanager.models import Show

class ShowAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basics', {'fields': ['name', 'day', 'starttime', 'stoptime', 'hosts', 'tagline', 'description',]}),
        ('Contact', {'fields': ['website', 'email', 'twitter', 'facebook']}),
    ]
admin.site.register(Show, ShowAdmin)
