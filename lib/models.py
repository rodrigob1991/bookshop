from django.db import models
from django.utils import timezone
from datetime import datetime, date, time, timedelta
# Create your models here.

class Libro(models.Model):
	titulo=models.CharField(max_length=255)
	isbn=models.CharField(max_length=13)
	prestamo=models.DateTimeField(blank=True,null=True)
	devolucion=models.DateField(blank=True,null=True)
	cliente=models.ForeignKey("Cliente",null=True,blank=True,default=None)
	

	def tiempo_prestamo(self):
		self.prestamo=datetime.now()
		self.devolucion=self.prestamo + timedelta(days=15)
		self.save()
           
	def __str__(self):
		return "{} ({})".format(self.titulo,self.isbn)

	#def get_absolute_url(self):
		#return reverse("libro", args=(self.id,))

class Cliente(models.Model):
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	cedula=models.CharField(max_length=8,unique=True)
	telefono=models.CharField(max_length=20,unique=True)
	email=models.EmailField(unique=True,null=True,blank=True)

	def __str__(self):
		return self.nombre + " "+self.apellido



