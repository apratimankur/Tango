from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
		
class Person(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

admin.site.register(Person)