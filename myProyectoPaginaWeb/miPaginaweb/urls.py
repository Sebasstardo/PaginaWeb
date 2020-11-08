from django.contrib import admin
from django.urls import path, include
from .views import index,galeria,formulario,contacto,nosotros,login,logout_vista,insumoAdmin, insumoEliminar,insumoBuscar,insumoActualizar

urlpatterns = [
    path('',index,name='IND'),
    path('galeria/',galeria,name='GALE' ),
    path('formulario/',formulario,name='FORC'),
    path('contacto',contacto,name='CON'),
    path('nosotros',nosotros,name='NOS'),
    path('entrar/',login,name='LOGIN'),
    path('salir/',logout_vista,name='LOGOUT'),
    path('admin_insumo/',insumoAdmin,name='INSADM'),
    path('eliminar_insumo/<id>',insumoEliminar, name='INSDEL'),
    path('actualizar_insumo/<id>',insumoBuscar,name='INSUPD'),
    path('modificar/',insumoActualizar,name='UPDATE')
]
