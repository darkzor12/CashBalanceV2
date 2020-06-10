from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from basic_app.models import Venituri,Cheltuieli
from basic_app.forms import VenituriForm,CheltuieliForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
from matplotlib import pylab
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io import *
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
# Create your views here.
############
#CBV
############
class DashBoardView(LoginRequiredMixin,TemplateView):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        v = Venituri.objects.all()
        c = Cheltuieli.objects.all()
        vi = sum([x.sumaVenit for x in v])
        ci = sum([x.sumaCheltuita for x in c])
        sold =  vi - ci
        context['venituri_total'] = vi
        context['cheltuieli_total'] = ci
        context['sold'] = sold
        return context
    template_name='dashboard.html'

class AboutView(TemplateView):
    template_name='about.html'

class ContactView(LoginRequiredMixin,TemplateView):
    template_name='contact.html'

@login_required
def chart(request):
    cumparaturi=Cheltuieli.objects.filter(categorie='Cumparaturi')
    masina=Cheltuieli.objects.filter(categorie='Masina')
    casa=Cheltuieli.objects.filter(categorie='Casa')
    timpLiber=Cheltuieli.objects.filter(categorie='Timp Liber')
    diverse=Cheltuieli.objects.filter(categorie='Diverse')

    vCumparaturi = sum([x.sumaCheltuita for x in cumparaturi])
    vMasina = sum([x.sumaCheltuita for x in masina])
    vCasa = sum([x.sumaCheltuita for x in casa])
    vtimpLiber = sum([x.sumaCheltuita for x in timpLiber])
    vDiverse = sum([x.sumaCheltuita for x in diverse])

    plt.close()

    labels=['Cumparaturi','Masina','Casa','Timp Liber','Diverse']
    ydata=[vCumparaturi,vMasina,vCasa,vtimpLiber,vDiverse]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','purple']
    explode = (0.1, 0, 0, 0,0)
    plt.pie(ydata, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'rapoarte.html',{'graphic':graphic})


class CheltuieliListView(LoginRequiredMixin,ListView):
    model = Cheltuieli

    def get_queryset(self):
        return Cheltuieli.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')

class VenituriListView(LoginRequiredMixin,ListView):
    model = Venituri

    # def get_queryset(self):
    #     v = Venituri.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')
    #     c = Cheltuieli.objects.all()
    #     return v | c
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        v = Venituri.objects.all()
        c = Cheltuieli.objects.all()
        vi = sum([x.sumaVenit for x in v])
        ci = sum([x.sumaCheltuita for x in c])
        sold =  vi - ci
        context['venituri_list'] = v
        context['venituri_total'] = vi
        context['cheltuieli_total'] = ci
        context['sold'] = sold
        return context


class CheltuieliDetailView(LoginRequiredMixin,DetailView):
    model = Cheltuieli

class VenituriDetailView(LoginRequiredMixin,DetailView):
    model = Venituri

class CreateCheltuieliView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='basic_app/cheltuieli_list.html'

    form_class = CheltuieliForm
    model = Cheltuieli


class CreateVenituriView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='basic_app/venituri_list.html'

    form_class = VenituriForm
    model = Venituri


class VenituriUpdateView(LoginRequiredMixin, UpdateView):
    login_url='/login/'
    redirect_field_name='basic_app/venituri_list.html'
    form_class = VenituriForm
    model = Venituri

class CheltuieliUpdateView(LoginRequiredMixin, UpdateView):
    login_url='/login/'
    redirect_field_name='basic_app/cheltuieli_list.html'
    form_class = CheltuieliForm
    model = Cheltuieli

class VenituriDeleteView(LoginRequiredMixin, DeleteView):
    model = Venituri
    success_url = reverse_lazy('venituri_list')

class CheltuieliDeleteView(LoginRequiredMixin, DeleteView):
    model = Cheltuieli
    success_url = reverse_lazy('cheltuieli_list')


########################
# FUNCS
#######################
