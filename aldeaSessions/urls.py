from django.conf.urls import url, patterns
from aldeaSessions.views import *

urlpatterns = patterns(
    '',
    url(
        r'^password/reset/$',
        'aldeaSessions.views.password_reset',
        {
            'post_reset_redirect': 'password_reset_done',
            'template_name': 'registrations/password_reset_form.html',
            'email_template_name': 'registrations/password_reset_email.html',
            'html_email_template_name': 'registrations/html_password_reset_email.html',
        },
        name="password_reset"
    ),
    url(
        r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {
            'template_name': 'registrations/password_reset_done.html'
        },
        name="password_reset_done"
    ),
    url(
        r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {
            'post_reset_redirect': 'password_done',
            'template_name': 'registrations/password_reset_confirm.html'
        },
        name="password_reset_confirm"
    ),
    url(
        r'^password/done/$',
        'django.contrib.auth.views.password_reset_complete',
        {
            'template_name': 'registrations/password_reset_complete.html'

        },
        name='password_done'
    ),

    url(r'^$',
        'aldeaSessions.views.login_request',
        name='login'),
    url(
        r'^accounts/generateKey/(?P<pk>\d+)/$',
        'aldeaSessions.views.generate_key',
        name='generate_key'),
    url(
        r'^register/$',
        'aldeaSessions.views.user_registration',
        name='register'),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/'
        },
        name='logout'),
    url(
        r'^noticia/nueva/$',
        NoticiaView.as_view(),
        name='noticia'
    ),
    url(
        r'^noticia/lista/$',
        NoticiaListView.as_view(),
        name='noticias_list'
    ),
    url(
        r'^noticia/eliminar/(?P<id>\d+)$',
        'aldeaSessions.views.eliminarNoticia',
        name='eliminar-noticia'
    ),
)
