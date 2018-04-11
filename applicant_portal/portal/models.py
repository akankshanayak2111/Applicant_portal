from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Applicant(models.Model):

	"""
		Model for Applicant
	"""

	id = models.AutoField(serialize=False, primary_key=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200, unique=True)
	phone = models.IntegerField(unique=True)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zipcode = models.IntegerField()
	application_status = models.CharField(max_length=100, default='applied')
	application_date = models.DateField(db_index=True, default=timezone.now)
	# created_at
	# updated_at
	


	def __str__(self):
		return '%s %s %s %s %s' % (self.id, self.name, self.email, self.phone, self.application_status)
