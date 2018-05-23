"""aldea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, ListView
from blog.models import Noticia
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='blog/inicio.html'), name='inicio'),
    url(r'^nosotros/$', TemplateView.as_view(template_name='blog/nosotros.html'), name='nosotros'),
    url(r'^noticias/$', ListView.as_view(template_name='blog/noticias.html', model=Noticia), name='noticias'),
    url(r'^recursos/alimentacion/$', TemplateView.as_view(template_name='blog/alimentacion.html'), name='alimentacion'),
    url(r'^recursos/alimentacion/recetas/$', TemplateView.as_view(template_name='blog/recetas.html'), name='recetas'),
    url(r'^recursos/alimentacion/lacteos/$', TemplateView.as_view(template_name='blog/lacteos.html'), name='lacteos'),
    url(r'^recursos/alimentacion/gluten/$', TemplateView.as_view(template_name='blog/gluten.html'), name='gluten'),
    url(r'^recursos/peliculas/$', TemplateView.as_view(template_name='blog/peliculas.html'), name='peliculas'),
    url(r'^recursos/centros/$', TemplateView.as_view(template_name='blog/centros.html'), name='centros'),
    url(r'^recursos/enlaces/$', TemplateView.as_view(template_name='blog/enlaces.html'), name='enlaces'),
    url(r'^recursos/manual/$', TemplateView.as_view(template_name='blog/manual.html'), name='manual'),
    url(r'^recursos/libro/$', TemplateView.as_view(template_name='blog/libro.html'), name='libro'),
    url(r'^preguntas/$', TemplateView.as_view(template_name='blog/preguntas.html'), name='preguntas'),
    url(r'^contacto/$', TemplateView.as_view(template_name='blog/contacto.html'), name='contacto'),
    url(r'^aldea/$', TemplateView.as_view(template_name='blog/aldea.html'), name='aldea'),
    url(r'^admin/', include(admin.site.urls)),
] + staticfiles_urlpatterns()