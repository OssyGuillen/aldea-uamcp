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
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='blog/home.html'), name='home'),
    url(r'^aldea/$', TemplateView.as_view(template_name='blog/base_aldea.html'), name='aldea'),
    url(r'^contacto/$', TemplateView.as_view(template_name='blog/contact.html'), name='contacto'),
    url(r'^nosotros/$', TemplateView.as_view(template_name='blog/doctors.html'), name='nosotros'),
    url(r'^noticias/$', TemplateView.as_view(template_name='blog/blog.html'), name='noticias'),
    url(r'^preguntas/$', TemplateView.as_view(template_name='blog/preguntas_frecuentes.html'), name='preguntas'),
    url(r'^recursos/alimentacion/$', TemplateView.as_view(template_name='blog/alimentacion.html'), name='alimentacion'),
    url(r'^recursos/alimentacion/gluten/$', TemplateView.as_view(template_name='blog/gluten.html'), name='gluten'),
    url(r'^recursos/alimentacion/lacteos/$', TemplateView.as_view(template_name='blog/lacteos.html'), name='lacteos'),
    url(r'^recursos/alimentacion/recetas/$', TemplateView.as_view(template_name='blog/recetas.html'), name='recetas'),
    url(r'^recursos/centros/$', TemplateView.as_view(template_name='blog/centros.html'), name='centros'),
    url(r'^recursos/enlaces/$', TemplateView.as_view(template_name='blog/enlaces.html'), name='enlaces'),
    url(r'^recursos/libro/$', TemplateView.as_view(template_name='blog/libro.html'), name='libro'),
    url(r'^recursos/manual/$', TemplateView.as_view(template_name='blog/manual.html'), name='manual'),
    url(r'^recursos/peliculas/$', TemplateView.as_view(template_name='blog/peliculas.html'), name='peliculas'),
    url(r'^admin/', include(admin.site.urls)),
] + staticfiles_urlpatterns()