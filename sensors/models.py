# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Sensors(models.Model):
	ps = models.FloatField(default=0)
	ss = models.FloatField(default=0)
	dw=models.FloatField(default=0)
	spw=models.FloatField(default=0)
	tpw=models.FloatField(default=0)
	serialId=models.CharField(max_length=10)
	def __str__(self):
		return str(self.temperature) +' '+ str(self.humidity)

