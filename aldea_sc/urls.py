from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import HomeView, DoctorsView

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
)
