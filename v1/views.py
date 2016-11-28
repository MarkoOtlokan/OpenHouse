from django.shortcuts import render
from MicroControlerScripts.FileUploads import *
import time

# Create your views here.
from rest_framework.views import APIView
from rest_framework import viewsets
from serializers import *
from models import *
from rest_framework.response import Response
from rest_framework.decorators import detail_route

# Create your views here.
class HouseViewSet(viewsets.ModelViewSet):
	serializer_class = HouseSerializer
	queryset = serializer_class.Meta.model.objects.all()

class FunctionViewSet(viewsets.ModelViewSet):
	serializer_class = FunctionSerializer
	queryset = serializer_class.Meta.model.objects.all()

	@detail_route(methods=['get'])
	def UploadArduinoCode(self, request, pk):
		function = self.get_object()
		terminalrasperrypi = function.Trasperrypi
		name = function.code.name.split('/')[-1]
		try:
			uploadArduinocode(terminalrasperrypi.ip
				,terminalrasperrypi.name
				,terminalrasperrypi.password
				,name
				,function.arduinoboard) 
			#time.sleep(100)
		except Exception as e:
			return Response({'eror': '%s' % e})
		return Response({'status': 'ok'})

	@detail_route(methods=['get'])
	def ArduinoSleep(self, request, pk):
		function = self.get_object()
		terminalrasperrypi = function.Trasperrypi
		try:
			arduinoToSleep(terminalrasperrypi.ip
				,terminalrasperrypi.name
				,terminalrasperrypi.password
				,function.arduinoboard) 
			time.sleep(100)
		except Exception as e:
			return Response({'eror': '%s' % e})
		return Response({'status': 'ok'})


class InmateViewSet(viewsets.ModelViewSet): 
	serializer_class = InmateSerializer
	queryset = serializer_class.Meta.model.objects.all()

class RasperrypiViewSet(viewsets.ModelViewSet):
	serializer_class = RasperrypiSerializer
	queryset = serializer_class.Meta.model.objects.all()
	#add upload code

class TerminalRasperrypiViewSet(viewsets.ModelViewSet):
	serializer_class = TerminalRasperrypiSerializer
	queryset = serializer_class.Meta.model.objects.all()

	@detail_route(methods=['get'])
	def ExecuteCode(self, request, pk):
		terminalrasperrypi = self.get_object()
		try:
			uploadCode(terminalrasperrypi.ip,terminalrasperrypi.name,terminalrasperrypi.password,terminalrasperrypi.code)	
		except Exception as e:
			return Response({'eror': '%s' % (e)})
		serializer = TerminalRasperrypiSerializer(terminalrasperrypi, context={'request': request}, many=True)        
		return Response({'status':'Transmited'})


class HouseNetworkViewSet(viewsets.ModelViewSet):
	serializer_class = HouseNetworkSerializer
	queryset = serializer_class.Meta.model.objects.all()
