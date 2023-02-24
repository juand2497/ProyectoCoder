from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Empresa
from AppCoder.models import Empleado
from AppCoder.models import Cliente
from AppCoder.models import Producto
from AppCoder.forms import *

# Create your views here.

def inicio(request):
    return render(request,'AppCoder/inicio.html')


def empresa(request):
    if request.method == 'POST':
        miFormulario = EmpresaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            empresa = Empresa(nombre_empresa=informacion['nombre_empresa'], direccion=informacion['direccion'])
            empresa.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = EmpresaFormulario()
    return render(request, "AppCoder/empresa.html", {"miFormulario":miFormulario}) 


def empleado(request):
    if request.method == 'POST':
        miFormulario = EmpleadoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            empleado = Empleado(nombre_empleado=informacion['nombre_empleado'], apellido_empleado=informacion['apellido_empleado'], puesto=informacion['puesto'], salario=informacion['salario'])
            empleado.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = EmpleadoFormulario()
    return render(request, "AppCoder/empleado.html", {"miFormulario":miFormulario}) 


def cliente(request):
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente(nombre_cliente=informacion['nombre_cliente'], apellido_cliente=informacion['apellido_cliente'], telefono=informacion['telefono'])
            cliente.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ClienteFormulario()
    return render(request, "AppCoder/cliente.html", {"miFormulario":miFormulario}) 


def producto(request):
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto(nombre_producto=informacion['nombre_producto'], valor=informacion['valor'], fecha=informacion['fecha'], entrega=informacion['entrega'])
            producto.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProductoFormulario()
    return render(request, "AppCoder/producto.html", {"miFormulario":miFormulario}) 


def busqueda(request):
    return render(request, "AppCoder/busqueda.html")


def buscar(request):
    if request.GET["nombre_empleado"]:
        nombre_empleado = request.GET['nombre_empleado']
        empleado = Empleado.objects.filter(nombre_empleado__icontains=nombre_empleado)
        return render(request, "AppCoder/resultadoBusqueda.html", {"nombre":nombre_empleado, "empleado":empleado})
    else:
        respuesta = "No hay datos" 
    return HttpResponse(respuesta)