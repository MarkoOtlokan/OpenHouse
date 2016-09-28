from rest_framework import serializers
from .models import Spisak, Tiket

class SpisakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spisak
        fields = ('id', 'ime')


class TiketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiket
        fields = (
            'id',
            'ime',
            'prezime',
            'adresa',
            'kolicina',
            'napomena',
            'stanje',
            'spisak',
        )
