from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from serializers import *
from rest_framework.response import Response
from rest_framework.decorators import detail_route

# Create your views here.
class HouseViewSet(viewsets.ModelViewSet):
	serializer_class = HouseSerializer
	queryset = serializer_class.Meta.model.objects.all()


class RasperrypiViewSet(viewsets.ModelViewSet):
	serializer_class = RasperrypiSerializer
	queryset = serializer_class.Meta.model.objects.all()
	#add upload code

class TerminalRasperrypiViewSet(viewsets.ModelViewSet):
	serializer_class = TerminalRasperrypiSerializer
	queryset = serializer_class.Meta.model.objects.all()
	#add upload code

class HouseNetworkViewSet(viewsets.ModelViewSet):
	serializer_class = HouseNetworkSerializer
	queryset = serializer_class.Meta.model.objects.all()