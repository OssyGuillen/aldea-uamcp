from django.contrib import admin
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'get_image',
        'autor',
        'categoria',
    )
    def get_image(self, obj):
        return obj.imagen.url
    get_image.short_description = 'Imagen'
    get_image.admin_order_field = 'Imagen__URL'
    search_fields = (
        'id',
        'titulo',
        'autor',
        'categoria',
    )


admin.site.register(Noticia, NoticiaAdmin)