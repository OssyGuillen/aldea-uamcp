from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	activation_key = models.CharField(max_length=40, blank=True)
	key_expires = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = u'User profiles'


class Noticia(models.Model):
	user = models.ForeignKey(User, null=True)
	imagen = models.ImageField(upload_to='images/noticias', null=True, blank=True)
	autor = models.CharField(max_length=100, default="Dra. Ana Cecilia Marquez")
	categoria = models.CharField(max_length=100, default="General")
	titulo = models.CharField(max_length=100, default="")
	text = models.TextField(default="")
	# parrafo = models.CharField(max_length=2000, default="")
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at',]