from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Libro,Cliente
from .form import ClienteForm

def prestar_libro(request,numero_libro):

	if request.method=="POST":
		form=ClienteForm(request.POST)
		form.is_valid()
		libro=Libro.objects.get(id=numero_libro)
		cedula= request.POST['cedula']
		try:	
			cliente=Cliente.objects.get(cedula=cedula)

		except: 
			return HttpResponseRedirect ('/libros_disponibles')

		libro.cliente=cliente
		libro.tiempo_prestamo()
		libro.save()
		return HttpResponseRedirect ('/libros_disponibles')
	else:
		clientes=Cliente.objects.all()
		cliente_form=ClienteForm()
		return render(request,'lib/prestar_libro.html',{'cliente_form':cliente_form,'clientes':clientes})

def libros_prestados(request):

	libros=Libro.objects.filter(cliente__isnull=False).order_by("devolucion")	
	return render(request,'lib/libros_prestados.html', {'libros': libros})

def libros_disponibles(request):

	libros=Libro.objects.filter(cliente__isnull=True)
	return render(request,'lib/libros_disponibles.html',{'libros':libros})

