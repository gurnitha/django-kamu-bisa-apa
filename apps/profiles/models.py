# apps/profiles/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import User

# Profile model
class Profile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		help_text='Field ini boleh dikosongkan.') 
	nama = models.CharField(
		max_length=50,
		blank=False,
		null=False,
		help_text='Field ini tidak boleh dikosongkan.') 
	perkenalan_singkat = models.CharField(
		max_length=150,
		blank=False,
		null=False,
		help_text='Field ini tidak boleh dikosongkan.') 
	gambar_profil = models.ImageField(
		upload_to='profiles/',
		default='profiles/user-default.png',
		blank=True,
		null=True,
		help_text='Field ini boleh dikosongkan.') 
	biograpi = models.TextField(
		blank=True,
		null=True,
		help_text='Field ini boleh dikosongkan.') 
	dibuat = models.DateTimeField(auto_now_add=True) 
	diupdate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nama


# Skill model
class Skill(models.Model):
	owner = models.ForeignKey(
		Profile,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		help_text='Field ini boleh dikosongkan.') 
	skill = models.CharField(
		max_length=50,
		blank=True,
		null=True,
		help_text='Field ini boleh dikosongkan.')
	dibuat = models.DateTimeField(auto_now_add=True) 
	diupdate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.skill