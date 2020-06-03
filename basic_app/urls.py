from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$', views.DashBoardView.as_view(), name='dashboard'),
    url(r'^about/$', views.AboutView.as_view(), name="about"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact"),
    url(r'^cheltuieli/$', views.CheltuieliListView.as_view(),name="cheltuieli_list"),
    url(r'^venituri/$', views.VenituriListView.as_view(),name="venituri_list"),
    url(r'^venituri/(?P<pk>\d+)$', views.VenituriDetailView.as_view(),name='venituri_detail'),
    url(r'^cheltuieli/(?P<pk>\d+)$', views.CheltuieliDetailView.as_view(),name='cheltuieli_detail'),
    url(r'^venituri/new/$', views.CreateVenituriView.as_view(),name='venituri_new'),
    url(r'^cheltuieli/new/$', views.CreateCheltuieliView.as_view(),name='cheltuieli_new'),
    url(r'^venituri/(?P<pk>\d+)/edit/$', views.VenituriUpdateView.as_view(),name='venituri_update'),
    url(r'^cheltuieli/(?P<pk>\d+)/edit/$', views.CheltuieliUpdateView.as_view(),name='cheltuieli_update'),
    url(r'^venituri/(?P<pk>\d+)/remove/$', views.VenituriDeleteView.as_view(), name='venituri_remove'),
    url(r'^cheltuieli/(?P<pk>\d+)/remove/$', views.CheltuieliDeleteView.as_view(), name='cheltuieli_remove')
]
