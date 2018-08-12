#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import datetime
import random
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import *
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.views import generic
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.csrf import csrf_protect
from django.template.response import TemplateResponse
from django.views.defaults import page_not_found
from blog.models import Noticia
from blog.forms import *
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from cloudinary.forms import cl_init_js_callbacks
import cloudinary.uploader
import cloudinary
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import logout

class HomeView(generic.TemplateView):
    template_name = 'home.html'


class DoctorsView(generic.TemplateView):
    template_name = 'doctors.html'


class PreguntasView(generic.TemplateView):
    template_name = 'preguntas_frecuentes.html'


class AlimentacionView(generic.TemplateView):
    template_name = 'alimentacion.html'


class RecetasView(generic.TemplateView):
    template_name = 'recetas.html'


class GlutenView(generic.TemplateView):
    template_name = 'gluten.html'


class LacteosView(generic.TemplateView):
    template_name = 'lacteos.html'


class EnlacesView(generic.TemplateView):
    template_name = 'enlaces.html'


class CentrosView(generic.TemplateView):
    template_name = 'centros.html'


class PeliculasView(generic.TemplateView):
    template_name = 'peliculas.html'


class ManualView(generic.TemplateView):
    template_name = 'manual.html'

class LibroView(generic.TemplateView):
    template_name = 'libro.html'

class NoticiasView(generic.TemplateView):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        self.object_list = []
        context = super(
            NoticiasView, self).get_context_data(**kwargs)
        noticias = Noticia.objects.all()
        context['noticias'] = noticias
        return self.render_to_response(context)

class AldeaView(generic.TemplateView):
    template_name = 'base_aldea.html'
    
#Sesion Noticia

class NoticiaView(generic.CreateView):
    template_name = "noticia.html"
    form_class = NoticiaForm
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = NoticiaForm
        return self.render_to_response(context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save()
            #noticia.user = request.user
            noticia.save()
            return HttpResponseRedirect(
                reverse_lazy('noticias_list'))
        else:
            return render(request, self.template_name, {'form': form})


@login_required 
def modificarNoticia(request, id):
    template_name = "noticia_mod.html"
    noticia = Noticia.objects.get(pk=id)
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            noticia = form.save()
            #noticia.user = request.user
            noticia.save()
            return HttpResponseRedirect(
                reverse_lazy('noticias_list'))
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, template_name, {'form': form})



class NoticiaListView(ListView):
    template_name = 'noticia_list.html'
    model = Noticia
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        self.object_list = []
        context = super(
            NoticiaListView, self).get_context_data(**kwargs)
        noticias = Noticia.objects.all()
        context['noticias'] = noticias
        #print("Image:" + noticia.image)
        return self.render_to_response(context)

@login_required 
def eliminarNoticia(request, id):
    noticia = Noticia.objects.get(pk=id)
    if (noticia.imagen.url): # Si existe imagen la borramos de cloduinary
        cloudinary.uploader.destroy(noticia.imagen.public_id,invalidate=True)
    noticia.delete()
    return HttpResponseRedirect(reverse_lazy('noticias_list'))
    
    
#Contacto

class contactoView(generic.CreateView):
    template_name = "blog/contacto.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        msj = request.POST.get( 'message', "")
        email = request.POST.get('email', "") 
        name = request.POST.get('fname', "")
        #print('ENVIAR',msj,email,name)
        mensaje = 'Correo proveniente del blog http://unidadautismo.herokuapp.com \n\n'
        mensaje = mensaje + '\n\nEnviado por: ' + name + '\n\nEmail: ' + email + '\n\nMensaje: \n\n' + msj
        envio = send_mail('[Mensaje del Blog]', mensaje, email, ['unidadautismomaternidadcom@gmail.com'], fail_silently=False)
        #print(envio)
        if (envio):
            messages.success(request, "Mensaje enviado correctamente!")
        else:
            messages.warning(request, 'Ha ocurrido un Error, su mensaje no se ha enviado')
        return render(request, self.template_name)
        
#Cerrar sesion

@login_required 
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect('/noticias')