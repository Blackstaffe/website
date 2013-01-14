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
    stoptime = models.TimeField()
    hosts = models.CharField(max_length=100)
    tagline = models.TextField(max_length=200)
    description = models.TextField(max_length=2000)
    website = models.URLField()
    email = models.EmailField(max_length=254)
    twitter = models.CharField(max_length=15)
    facebook = models.URLField()
    
