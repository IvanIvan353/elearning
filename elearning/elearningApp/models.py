from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class User(models.Model)
	firstName = models.CharField(max_length=25, null=False, blank=False)
	lastName = models.CharField(max_length=25, null=False, blank=False)
	username = models.Charfield(min_length=5, max_length=25, null=false)
	password = models.Charfield(min_length=5, max_length=25, null=false)
	dateOfBirth = models.DateTimeField('date of birth')
	role = models.ForeignKey(Role, on_delete=models.CASCADE)

@python_2_unicode_compatible
class Role	
	name = models.CharField(max_length=25, null=False, blank=False)

@python_2_unicode_compatible
class Permission
	name = models.CharField(max_length=25, null=False, blank=False)
	roles = models.ManyToManyField(Role)	
