import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Profiles(models.Model):
    user = models.OneToOneField(get_user_model())
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

    owner = models.ForeignKey(Profiles)
    contributors = models.ManyToManyField(Profiles)

    website = models.URLField()
    documentation = models.URLField()

    def is_active(self):
        return self.last_update >= timezone.now() - datetime.timedelta(days=14)
