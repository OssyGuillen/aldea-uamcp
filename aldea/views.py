from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import Context
from aldeaSessions.models import Noticia


class NoticiasView(TemplateView):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        self.object_list = []
        context = super(   NoticiasView, self).get_context_data(**kwargs)

        context['noticias'] = Noticia.objects.all()
        return self.render_to_response(context)