from django import forms
from basic_app.models import Cheltuieli,Venituri

class CheltuieliForm(forms.ModelForm):

    class Meta():
        model = Cheltuieli
        fields = ('user','sumaCheltuita','create_date','categorie','note','atasament_cheltuieli' )

class VenituriForm(forms.ModelForm):
    class Meta():
        model = Venituri
        fields = ('user','sumaVenit', 'descriere', 'create_date','note','atasament_venituri')
