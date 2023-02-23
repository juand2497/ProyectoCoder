from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Empresa

# Create your views here.
def empresa(self):
    empresa = Empresa(nombre_empresa="Postobon", direccion="Dosquebradas") 
    empresa.save()
    documentoDeTexto = f"--> Empresa: {empresa.nombre_empresa} direccion: {empresa.direccion}"
    return HttpResponse(documentoDeTexto)