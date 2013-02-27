from django.db import models

# Show database model
class Show(models.Model):
    # Basic Info 
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True, max_length=25)
    day = models.CharField(max_length=10, choices=[
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'), 
        ('Thursday', 'Thursday'), 
        ('Friday', 'Friday'), 
        ('Saturday','Saturday')])
    timeslot = models.TimeField()
    startdate = models.DateField()
    biweekly = models.BooleanField()
    length = models.IntegerField(choices=[
        (30, 'Half-hour'),
        (60, 'Hour'),
        (90, 'Hour and a half'),
        (120, 'Two hours' ),
        (150, 'Two and a half hours'),
        (180, 'Three hours')])
    genre = models.CharField(max_length=15, choices=[
        ('Eclectic', 'Eclectic'),
        ('Spoken Word', 'Spoken Word'),
        ('News', 'News'),
        ('Roots', 'Roots'),
        ('Hip-Hop', 'Hip-Hop'),
        ('Cultural', 'Cultural'),
        ('Loud', 'Loud'),
        ('Specialty', 'Specialty')])
    description = models.TextField(max_length=2000)
    inactive = models.BooleanField()
    # Contact Info 
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    twitter = models.CharField(max_length=15, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    def __unicode__(self):
        return self.name    
class Host(models.Model):
    show = models.ForeignKey(Show)
    host = models.CharField(max_length=200)
    def __unicode__(self):
        return self.host
