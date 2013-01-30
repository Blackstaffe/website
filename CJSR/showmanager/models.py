from django.db import models

# Show database model
class Show(models.Model):
    name = models.CharField(max_length=20)
    day = models.CharField(max_length=10, choices=[(
        'Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'), 
        ('Thursday', 'Thursday'), 
        ('Friday', 'Friday'), 
        ('Saturday','Saturday')])
    starttime = models.TimeField()
    length = models.TimeField() # TODO > add choices
    tagline = models.TextField(max_length=200)
    description = models.TextField(max_length=2000)
    def __unicode__(self):
        return self.name    

class Hosts(models.Model):
    show = models.ForeignKey(Show)
    hosts = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Contact(models.Model):
    host = models.ForeignKey(Hosts)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    twitter = models.CharField(max_length=15, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    def __unicode__(self):
        return self.name

