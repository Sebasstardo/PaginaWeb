from django.contrib import admin
from django.urls import path, include
from .views import index,galeria,formulario,contacto,nosotros,producto,login,logout_vista,admin_productos,eliminar,actualizar,actualiza

urlpatterns = [
    path('',index,name='IND'),
    path('galeria/',galeria,name='GALE' ),
    path('formulario/',formulario,name='FORC'),
    path('contacto',contacto,name='CON'),
    path('nosotros',nosotros,name='NOS'),
    path('producto',producto,name='FORP'),
    path('dentrar/',login,name='LOGIN'),
    path('Salir/',logout_vista,name='LOGOUT'),
    path('admin_productos/',admin_productos,name='ADP'),
    path('eliminar_producto/<id>',eliminar, name='ELIM'),
    path('actualizar_producto/<id>',actualizar,name='ACTP'),
    path('actualiza/',actualiza,name='ACTPROD')
]
