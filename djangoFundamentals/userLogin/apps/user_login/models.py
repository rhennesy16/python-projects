from __future__ import unicode_literals
from django.db import models

class dojos(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class ninjas(models.Model):
	dojo = models.ForeignKey(Dojo, related_name="ninjas")
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
