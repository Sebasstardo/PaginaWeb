from django.shortcuts import render
from .models import Producto, Insumo, SliderIndex, MisionVision, Galeria
#importa la tabla de usuarios al admin

from django.contrib.auth.models import User

#importar librerias de autentificacion

from django.contrib.auth import authenticate,logout,login as login_autent

#agregar una decoracion que permite evitar el ingreso a las paginas
#sin estar registrado

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def logout_vista(request):
    logout(request)
    autos = SliderIndex.objects.all()
    return render(request,'index.html', {'autos' : autos})

def login(request):
    sw = 0
    autos = SliderIndex.objects.all()
    if request.POST:
        usuario = request.POST.get("usuario")
        password = request.POST.get("clave")
        us = authenticate(request, username = usuario, password = password)
        if us is not None and us.is_active:
            login_autent(request,us)
            return render(request,'index.html', {'user' : us, 'autos' : autos})
        else:
            sw = 1
            return render(request,'login.html', {'sw' : sw})
    return render(request,'login.html')


def index(request):
    autos = SliderIndex.objects.all()
    return render(request,'index.html', {'autos' : autos})


def galeria(request):
    galeria = Galeria.objects.all()
    return render(request,'galeria.html', {'galeria' : galeria})


def formulario(request):
    if request.POST:
        autos = SliderIndex.objects.all()
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        correo = request.POST.get("txtCorreo")
        usuario = request.POST.get("txtUsuario")
        clave1 = request.POST.get("clave1")
        clave2 = request.POST.get("clave2")
        try:
            u = User.objects.get(email = correo)
            sw = 3
            return render(request, 'formRegistro.html', {'sw' : sw})
        except:
            pass
        try:
            u = User.objects.get(username = usuario)         
            sw = 1
            return render(request,'formRegistro.html', {'sw' : sw})
        except:
            if clave1 != clave2:               
                sw = 2
                return render(request,'formRegistro.html', {'sw' : sw})
            u = User()
            u.first_name = nombre
            u.last_name = apellido
            u.email = correo
            u.username = usuario
            u.set_password(clave1)
            u.save()
            us = authenticate(request, username = usuario, password = clave1)
            login_autent(request, us)
            return render(request,'index.html', {'user' : us, 'autos' : autos}) 
    return render(request,'formRegistro.html')


def contacto(request):
    return render(request,'contacto.html')


def nosotros(request):
    myv = MisionVision.objects.all()
    return render(request,'nosotros.html',{'myv' : myv})

@login_required(login_url = '/entrar/')
@permission_required ('miPaginaweb.add_insumo', login_url ='/entrar/') 
def producto (request):
    sw = 0
    productos = Producto.objects.all()  
    if request.POST:
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        stock = request.POST.get ("stock")
        desc = request.POST.get("desc")
        producto = request.POST.get("producto")
        obj_producto = Producto.objects.get(tipo = producto)

        ins = Insumo(
            nombre = nombre,
            precio = precio,
            stock = stock,
            descripcion = desc,
            Producto = obj_producto
        )
        ins.save()
        sw = 1
        return render (request, 'producto.html',{'lista_productos' : productos, 'msg' : 'Grabo', 'sw' : sw})

    return render (request, 'producto.html',{'lista_productos' : productos, 'msg' : 'nn', 'sw' : sw})

@login_required(login_url = '/entrar/')
@permission_required ('miPaginaweb.add_insumo', login_url ='/entrar/')    
def admin_productos(request):
    sw = 0
    productos = Producto.objects.all()
    insumo = Insumo.objects.all()
    if request.POST:
        accion = request.POST.get("accion")
        if accion =="Actualizar":
            nombre = request.POST.get("nombre")
            precio = request.POST.get("precio")
            stock = request.POST.get ("stock")
            desc = request.POST.get("desc")
            producto = request.POST.get("producto")
            obj_producto = Producto.objects.get(tipo=producto)
            try:
                ins = Insumo.objects.get(nombre=nombre)
                ins.precio = precio
                ins.stock = stock
                ins.desc = desc
                ins.producto = obj_producto
                ins.save()
                sw = 4
            except:
                sw = 3
            return render (request,'adminProd.html',{'lista_i':insumo,'lista_productos':productos,'msg':'Grabo','sw':sw})

        if accion =="Eliminar":
            nombre = request.POST.get("nombre")
            try:
                ins =Insumo.objects.get(nombre=nombre)
                ins.delete()
                sw = 2
            except:
                sw = 3
            return render (request,'adminProd.html',{'lista_i':insumo,'lista_productos':productos,'sw':sw})

        if accion=="Registrar":
            nombre = request.POST.get("nombre")
            precio = request.POST.get("precio")
            stock = request.POST.get ("stock")
            desc = request.POST.get("desc")
            producto = request.POST.get("producto")
            obj_producto = Producto.objects.get(tipo=producto)

            ins = Insumo(
                nombre = nombre,
                precio = precio,
                stock = stock,
                descripcion = desc,
                Producto = obj_producto
            )
            ins.save()
            sw = 1
            return render (request,'adminProd.html',{'lista_i':insumo,'lista_productos':productos,'msg':'Grabo','sw':sw})


    return render(request, 'adminProd.html',{'lista_i':insumo,'lista_productos':productos})


@login_required(login_url = '/entrar/')
@permission_required ('miPaginaweb.add_insumo', login_url ='/entrar/') 
def eliminar(request,id):
    try:
        ins = Insumo.objects.get(nombre = id)
        ins.delete()
        sw = 2
    except:
        sw = 3
    productos = Producto.objects.all()
    insumo = Insumo.objects.all()
    return render(request, 'adminProd.html',{'lista_i':insumo,'lista_productos':productos,'sw':sw})

@login_required(login_url = '/entrar/')
@permission_required ('miPaginaweb.add_insumo', login_url ='/entrar/') 
def actualizar(request,id):
    productos = Producto.objects.all()
    try:
        ins = Insumo.objects.get(nombre=id)
        sw = 4
        return render (request,'actualizarP.html',{'ins':ins,'lista_productos':productos,'sw':sw})
    except:
        sw = 3
   
    insumo = Insumo.objects.all()
    return render(request, 'adminProd.html',{'lista_i':insumo,'lista_productos':productos,'sw':sw})

@login_required(login_url = '/entrar/')
@permission_required ('miPaginaweb.add_insumo', login_url ='/entrar/') 
def actualiza(request):
    productos = Producto.objects.all()
    insumo = Insumo.objects.all()
    if request.POST:
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        stock = request.POST.get ("stock")
        desc = request.POST.get("desc")
        producto = request.POST.get("producto")
        obj_producto = Producto.objects.get(tipo=producto)
        try:
            ins = Insumo.objects.get(nombre = nombre)
            ins.precio = precio
            ins.stock = stock
            ins.desc = desc
            ins.producto = obj_producto
            ins.save()
            sw = 4
        except:
            sw = 3
    return render (request,'adminProd.html',{'lista_i':insumo,'lista_productos':productos,'msg':'Grabo','sw':sw})

       
      