from django.contrib import admin
from .models import Noticia

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