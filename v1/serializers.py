from rest_framework import serializers, viewsets, routers
from models import House, Rasperrypi, HouseNetwork, TerminalRasperrypi

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
			'code', 
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


