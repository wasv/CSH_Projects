import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    bio = models.TextField()
    website = models.URLField()

class Project(models.Model):
    STATE_CHOICES = (
        ('C','Concept'),
        ('O','Ongoing'),
        ('D','Done'),
        ('A','Abandoned')
    )
    title = models.CharField(max_length=140)
    description = models.TextField()
    last_update = models.DateField(timezone.now())
    state = models.CharField(max_length=1, choices=STATE_CHOICES)

    owner = models.ForeignKey(Profile, related_name="%(app_label)s_%(class)s_owner")
    contributors = models.ManyToManyField(Profile, related_name="%(app_label)s_%(class)s_contributors")

    website = models.URLField()
    documentation = models.URLField()

    def is_active(self):
        return self.last_update >= timezone.now() - datetime.timedelta(days=14)
