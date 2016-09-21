from django.shortcuts import render
from MicroControlerScripts.script1 import uploadCode

# Create your views here.
from rest_framework import viewsets
from serializers import *
from models import *
from rest_framework.response import Response
from rest_framework.decorators import detail_route
#import MicroControlerScripts.script1

# Create your views here.
class HouseViewSet(viewsets.ModelViewSet):
	serializer_class = HouseSerializer
	queryset = serializer_class.Meta.model.objects.all()

class FunctionViewSet(viewsets.ModelViewSet):
	serializer_class = FunctionSerializer
	queryset = serializer_class.Meta.model.objects.all()

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
		uploadCode(terminalrasperrypi.ip,terminalrasperrypi.name,terminalrasperrypi.password,terminalrasperrypi.code)	
		serializer = TerminalRasperrypiSerializer(terminalrasperrypi, context={'request': request}, many=True)        
		return Response(serializer.data)

class HouseNetworkViewSet(viewsets.ModelViewSet):
	serializer_class = HouseNetworkSerializer
	queryset = serializer_class.Meta.model.objects.all()