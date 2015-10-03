import datetime, os
from django.db import models
from django.utils import timezone
from django.conf import settings


def get_profile_url(instance, filename):
    (_,ext) = os.path.splitext(filename)
    uid = instance.user.id
    print('profile-pics/'+ uid + ext)
    return 'profile-pics/'+ uid + ext


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    bio = models.TextField()
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to=get_profile_url)

    def __str__(self):
        if hasattr(self.user, 'name'):
            return self.user.first_name + self.user.last_name + " (" + self.user.username + ")"
        else:
            return self.user.username


class Project(models.Model):
    STATE_CHOICES = (
        ('C','Concept'),
        ('O','Ongoing'),
        ('D','Done'),
        ('A','Abandoned')
    )
    title = models.CharField(max_length=140)
    description = models.TextField()
    last_update = models.DateField(default=timezone.now)
    state = models.CharField(max_length=1, choices=STATE_CHOICES)

    owner = models.ForeignKey(Profile, related_name="%(app_label)s_%(class)s_owner", blank=True)
    contributors = models.ManyToManyField(Profile, related_name="%(app_label)s_%(class)s_contributors", blank=True)

    website = models.URLField(blank=True)
    documentation = models.URLField(blank=True)

    def is_active(self):
        return self.last_update >= timezone.now() - datetime.timedelta(days=14)

    def __str__(self):
        return self.title + " (by " + self.owner.user.username + ")"
