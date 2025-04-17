# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Vessel(models.Model):

    #__Vessel_FIELDS__
    vessel_name = models.CharField(max_length=255, null=True, blank=True)
    vessel_type = models.CharField(max_length=255, null=True, blank=True)
    mmsi = models.CharField(max_length=255, null=True, blank=True)
    added_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    region = models.CharField(max_length=255, null=True, blank=True)

    #__Vessel_FIELDS__END

    class Meta:
        verbose_name        = _("Vessel")
        verbose_name_plural = _("Vessel")


class Logentry(models.Model):

    #__Logentry_FIELDS__
    added_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    id = models.IntegerField(null=True, blank=True)
    log_text = models.TextField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    lon = models.CharField(max_length=255, null=True, blank=True)
    catagory = models.IntegerField(null=True, blank=True)
    severity = models.IntegerField(null=True, blank=True)

    #__Logentry_FIELDS__END

    class Meta:
        verbose_name        = _("Logentry")
        verbose_name_plural = _("Logentry")



#__MODELS__END
