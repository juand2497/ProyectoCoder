from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicio, name="Inicio"), #primera vista
    path('empleado',views.empleado, name="Empleado"),
    path('empresa',views.empresa, name="Empresa"),
    path('cliente',views.cliente, name="Cliente"),
    path('producto',views.producto, name="Producto"),
    path('busqueda',views.busqueda, name="busqueda"),
    path('buscar/',views.buscar, name="Resultado"),
    
]