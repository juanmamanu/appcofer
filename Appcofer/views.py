from django.shortcuts import render
from django.http import HttpResponse

def saludar(request): #consulta o peticion 
	return HttpResponse("Hola Django - ") #response = respuesta 

def saludo_dos(request):
    return HttpResponse("este es otro saludo ")
# Create your views here.
#request consulta o peticion

def saludar_a(request, nombre):
    return HttpResponse(f"como estas {nombre}")

def mostrar_mi_template(request):
    return render(request,"appcofer/index.html")