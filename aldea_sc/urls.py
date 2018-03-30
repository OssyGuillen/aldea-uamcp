from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import HomeView, DoctorsView, PreguntasView, AlimentacionView, RecetasView, LacteosView, GlutenView, EnlacesView, CentrosView, PeliculasView, ManualView, ContactoView, NoticiasView, AldeaView, LibroView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aldea_sc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^session/', include('aldeaSessions.urls')),
    url(
        r'^$',
        HomeView.as_view(),
        name='home'
    ),
    url(
        r'^nosotros/$',
        DoctorsView.as_view(),
        name='nosotros'
    ),
    url(
        r'^preguntas/$',
        PreguntasView.as_view(),
        name='preguntas'
    ),
    url(
        r'^recursos/alimentacion/$',
        AlimentacionView.as_view(),
        name='alimentacion'
    ),
    url(
        r'^recursos/alimentacion/recetas/$',
        RecetasView.as_view(),
        name='recetas'
    ),
    url(
        r'^recursos/alimentacion/gluten/$',
        GlutenView.as_view(),
        name='gluten'
    ),
    url(
        r'^recursos/alimentacion/lacteos/$',
        LacteosView.as_view(),
        name='lacteos'
    ),
    url(
        r'^recursos/enlaces/$',
        EnlacesView.as_view(),
        name='enlaces'
    ),
    url(
        r'^recursos/centros/$',
        CentrosView.as_view(),
        name='centros'
    ),
    url(
        r'^recursos/peliculas/$',
        PeliculasView.as_view(),
        name='peliculas'
    ),
    url(
        r'^recursos/manual/$',
        ManualView.as_view(),
        name='manual'
    ),
    url(
        r'^recursos/libro/$',
        LibroView.as_view(),
        name='libro'
    ),
    url(
        r'^contacto/$',
        ContactoView.as_view(),
        name='contacto'
    ),
    url(
        r'^noticias/$',
        NoticiasView.as_view(),
        name='noticias'
    ),
    url(
        r'^aldea/$',
        AldeaView.as_view(),
        name='aldea'
    )
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

