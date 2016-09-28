from django.db import models

class Spisak(models.Model):
    ime = models.CharField(max_length=32)

    def __str__(self):
        return self.ime


class Tiket(models.Model):
    ime = models.CharField(max_length=32)
    prezime = models.CharField(max_length=32)
    adresa = models.CharField(max_length=50)
    kolicina = models.CharField(max_length=7)
    napomena = models.TextField()
    stanje = models.CharField(max_length=20, default="ne_isporuceno")
    spisak = models.ForeignKey(Spisak)

    def __str__(self):
        return self.adresa
