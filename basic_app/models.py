from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.

CATEGORIE_CHOICES= (
    ('Cumparaturi','Cumparaturi'),
    ('Masina', 'Masina'),
    ('Casa','Casa'),
    ('Timp Liber','Timp Liber'),
    ('Diverse','Diverse')
)
class Cheltuieli(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    sumaCheltuita = models.FloatField()
    # sumaTotalCheltuita = models.FloatField(blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    note = models.CharField(max_length=80, blank=True)
    atasament_cheltuieli = models.ImageField(upload_to='atasament_cheltuieli',null=True, blank=True)
    categorie = models.CharField(max_length=15, choices=CATEGORIE_CHOICES, default="diverse")

    def get_absolute_url(self):
        return reverse('cheltuieli_list')




class Venituri(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    sumaVenit = models.FloatField()
    descriere = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=timezone.now)
    note = models.CharField(max_length=80, blank=True)
    atasament_venituri = models.ImageField(upload_to='atasament_venituri', blank=True)

    def get_absolute_url(self):
        return reverse('venituri_list')
