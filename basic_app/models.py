from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Cheltuieli(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    sumaCheltuita = models.FloatField()
    # sumaTotalCheltuita = models.FloatField(blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    note = models.CharField(max_length=80)
    atasament_cheltuieli = models.ImageField(upload_to='atasament_cheltuieli',null=True, blank=True)
    # TODO CATEGORIE

    def get_absolute_url(self):
        return reverse('cheltuieli_list')




class Venituri(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    sumaVenit = models.FloatField()
    descriere = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=timezone.now)
    note = models.CharField(max_length=80)
    atasament_venituri = models.ImageField(upload_to='atasament_venituri', blank=True)

    def get_absolute_url(self):
        return reverse('venituri_list')




class Sold(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    baniCheltuiti = models.FloatField(blank=True)
    baniVenituri = models.FloatField(blank=True)
    sold = models.FloatField(blank=True)

    def addCheltuieli(self):
        self.baniCheltuiti = self.baniCheltuiti + self.sumaCheltuita
        self.save()
    def addVenituri(self):
        self.baniVenituri = self.baniVenituri + self.sumaVenit
        self.save()
    def interogareSold(self):
        self.sold= self.addVenituri - self.baniCheltuiti
        self.save()
        return sold
