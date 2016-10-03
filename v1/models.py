from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Inmate(models.Model):
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	username = models.CharField(max_length=32)
	password = models.CharField(max_length=32)
	house = models.ForeignKey('House')

	def __str__(self):
		return self.username

class Function(models.Model):
	name = models.CharField(max_length=32)
	code = models.FileField(upload_to='MicroControlerScripts/RassperrypiCodes/Functions')
	command = models.CharField(max_length=32,blank=True,null=True)
	Trasperrypi = models.ForeignKey('TerminalRasperrypi',blank=True,null=True)
	rasperrypi = models.ForeignKey('Rasperrypi',blank=True,null=True)

	def __str__(self):
		return self.name

class TerminalRasperrypi(models.Model):
	name = models.CharField(max_length=32)
	ip = models.CharField(max_length=32)
	code = models.FileField(upload_to='MicroControlerScripts/RassperrypiCodes')
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
	housenetwork = models.ForeignKey('HouseNetwork')
	terminalrasperrypi = models.ForeignKey('TerminalRasperrypi')

	def __str__(self):
		return self.name 

class Rasperrypi(models.Model):
	name = models.CharField(max_length=32)
	ip = models.CharField(max_length=32)
	code = models.FileField(upload_to='MicroControlerScripts/RassperrypiCodes')
	password = models.CharField(max_length=32)
	house = models.ForeignKey('House')

	def __str__(self):
		return self.name +':'+ self.ip

