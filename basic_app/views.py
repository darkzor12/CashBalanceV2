from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from basic_app.models import Venituri,Cheltuieli,Sold
from basic_app.forms import VenituriForm,CheltuieliForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
# Create your views here.
############
#CBV
############
class DashBoardView(LoginRequiredMixin,TemplateView):
    # TO DO
    template_name='dashboard.html'

class AboutView(TemplateView):
    template_name='about.html'

class CheltuieliListView(LoginRequiredMixin,ListView):
    model = Cheltuieli

    def get_queryset(self):
        return Cheltuieli.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')

class VenituriListView(LoginRequiredMixin,ListView):
    model = Venituri

    def get_queryset(self):
        return Venituri.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')

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
