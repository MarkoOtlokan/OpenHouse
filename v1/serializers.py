from rest_framework import serializers, viewsets, routers
from models import *

# Serializers define the API representation.
class TerminalRasperrypiSerializer(serializers.ModelSerializer):
	class Meta:
		model = TerminalRasperrypi
		fields = (
			'id',
			'name',
			'ip',
			'code',
			'password',
			)

class FunctionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Function
		fields = (
			'id',
			'name',
			'code',
			'command',
			'Trasperrypi',
			'rasperrypi',
			'arduinoboard',
			)

class InmateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Inmate
		fields = (
			'id',
			'first_name',
			'last_name',
			'username',
			'password',
			'house',
			)

class HouseNetworkSerializer(serializers.ModelSerializer):
	class Meta:
		model = HouseNetwork
		fields = ('id', 'name')

class HouseSerializer(serializers.ModelSerializer):
	class Meta:
		model = House
		fields = (
			'id', 
			'name', 
			'housenetwork',
			'terminalrasperrypi',
			)

class RasperrypiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rasperrypi
		fields = (
			'id',
			'name',
			'ip',
			'code',
			'password',
			'house',
			)