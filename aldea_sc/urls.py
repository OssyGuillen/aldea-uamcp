from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import HomeView, DoctorsView, PreguntasView, AlimentacionView, RecetasView, LacteosView, GlutenView

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
)
