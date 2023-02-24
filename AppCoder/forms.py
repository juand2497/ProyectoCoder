from django import forms 

class EmpresaFormulario(forms.Form):
    nombre_empresa = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=80)
    
class EmpleadoFormulario(forms.Form):
    nombre_empleado = forms.CharField(max_length=40)
    apellido_empleado = forms.CharField(max_length=40)
    puesto = forms.CharField(max_length=30)
    salario = forms.FloatField()

class ClienteFormulario(forms.Form):
    nombre_cliente = forms.CharField(max_length=40)
    apellido_cliente = forms.CharField(max_length=40)
    telefono = forms.IntegerField()

class ProductoFormulario(forms.Form):
    nombre_producto = forms.CharField(max_length=40)
    valor = forms.FloatField()
    fecha = forms.DateField()
    entrega = forms.BooleanField()