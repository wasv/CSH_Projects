import datetime, os
from django.db import models
from django.utils import timezone
from django.conf import settings
from PIL import Image


def autoresize_image(image_path,out_path=None):
    if not out_path:
        out_path = image_path
    baseimg = Image.open(image_path)
    newsize = baseimg.size
    print(newsize)
    if baseimg.size[0] > settings.MAX_IMAGE_XSIZE:
        xratio = (settings.MAX_IMAGE_XSIZE/baseimg.size[0])
        newsize = (int(settings.MAX_IMAGE_XSIZE),int(baseimg.size[1]*xratio))
        baseimg = baseimg.resize(newsize,Image.ANTIALIAS)
    if baseimg.size[1] > settings.MAX_IMAGE_YSIZE:
        baseimg = baseimg.crop((0,0,newsize[0],int(settings.MAX_IMAGE_YSIZE)))
    baseimg.save(out_path)


def get_project_path(instance, filename):
    (_,ext) = os.path.splitext(filename)
    uid = str(instance.id)
    print('project-pics/'+ uid + ext)
    return 'project-pics/'+ uid + ext


def get_profile_path(instance, filename):
    (_,ext) = os.path.splitext(filename)
    uid = str(instance.user.id)
    print('profile-pics/'+ uid + ext)
    return 'profile-pics/'+ uid + ext


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to=get_profile_path, blank=True)

    def __str__(self):
        if hasattr(self.user, 'name'):
            return self.user.first_name + self.user.last_name + " (" + self.user.username + ")"
        else:
            return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args,**kwargs)
        if self.picture:
            autoresize_image(self.picture.path)


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
    picture = models.ImageField(upload_to=get_project_path, blank=True)

    owner = models.ForeignKey(Profile, related_name="%(app_label)s_%(class)s_owner", blank=True)
    contributors = models.ManyToManyField(Profile, related_name="%(app_label)s_%(class)s_contributors", blank=True)

    website = models.URLField(blank=True)
    documentation = models.URLField(blank=True)

    def is_active(self):
        return self.last_update >= timezone.now() - datetime.timedelta(days=14)

    def __str__(self):
        return self.title + " (by " + self.owner.user.username + ")"

    def save(self, *args, **kwargs):
        super(Project, self).save(*args,**kwargs)
        if self.picture:
            autoresize_image(self.picture.path)