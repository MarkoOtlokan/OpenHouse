from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TerminalRasperrypi(models.Model):
	name = models.CharField(max_length=32)
	ip = models.CharField(max_length=32)
	code = models.TextField()
	password = models.CharField(max_length=32)

	def __str__(self):
		return self.name +':'+ self.ip

class HouseNetwork(models.Model):
	name = models.CharField(max_length=32)
	#add permisons

	def __str__(self):
		return self.name

class House(models.Model):
	name = models.CharField(max_length=32)	
	code = models.TextField()
	housenetwork = models.ForeignKey('HouseNetwork')
	terminalrasperrypi = models.ForeignKey('TerminalRasperrypi')

	def __str__(self):
		return self.name 

class Rasperrypi(models.Model):
	name = models.CharField(max_length=32)
	ip = models.CharField(max_length=32)
	code = models.TextField()
	password = models.CharField(max_length=32)
	house = models.ForeignKey('House')

	def __str__(self):
		return self.name +':'+ self.ip

