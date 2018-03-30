from django.contrib import admin
from aldeaSessions.models import *


class NoticiaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'imagen',
        'autor',
        'categoria',
    )
    search_fields = (
        'id',
        'titulo',
        'imagen',
        'autor',
        'categoria',
    )


admin.site.register(Noticia, NoticiaAdmin)