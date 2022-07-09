from django.shortcuts import render, redirect
<<<<<<< HEAD
<<<<<<< HEAD
from urllib import response
from django.http import HttpResponse
from .models import Usuario
=======
from .models import *
>>>>>>> 2f6b4c37de69e19b2f9d2c3f3db22fa8dbc8c572
=======
from .models import *
>>>>>>> Juan

# Create your views here.
def inventario(request):
    return render(request,'inventario.html')

def home(request):
    if 'usuario' not in request.session:
        return redirect('/login/')

    return render(request,'index.html')

def about(request):
    return render(request,'acerca_de.html')

def bandanas(request):
    return render(request,'bandanas.html')

def confirm(request):
    return render(request,'confirm.html')

def correas(request):
    return render(request,'correas.html')

def identificadores(request):
    return render(request,'identificadores.html')

def login(request):
    return render(request,'login-signin.html')

def perfil(request):
    return render(request,'perfil_usuario.html')

def carro(request):
    return render(request,'shopping-cart.html')

def donar(request):
    return render(request,'subscripcion.html')

<<<<<<< HEAD
<<<<<<< HEAD
def validarUsuario(request):
    v_email = request.POST.get('email')
    v_password = request.POST.get('password')

    try:
        usu=Usuario.objects.get(email=v_email, password=v_password)

        if usu:
            request.session['usuario'] = v_email
            return redirect('/perfil/')

    except:
        return redirect('/login/')
=======
=======
>>>>>>> Juan
def guardarProducto(request):
    
    v_idproducto=request.POST.get('idproducto')
    v_nomproducto=request.POST.get('nombre')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')

    nuevo=Producto()
    nuevo.idProducto=v_idproducto
    nuevo.nombre=v_nomproducto
    nuevo.stock=v_stockproducto
    nuevo.precio=v_preproducto

    Producto.save(nuevo)

    return redirect('/')
    
def eliminarProducto(request, p_idProducto):
    buscado=Producto.objects.get(idProducto=p_idProducto)
    if(buscado):
        Producto.delete(buscado)
        return redirect('/')

def buscarProducto(request, p_idProducto):
    buscado=Producto.objects.get(idProducto=p_idProducto)
    datos={'producto': buscado}
    return render(request, 'modificar.html', datos)

def guardarProductoModificado(request):
    v_idproducto=request.POST.get('idproducto')
    v_nomproducto=request.POST.get('nombre')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')

    buscado=Producto.objects.get(idProducto=v_idproducto)

    if(buscado):
        buscado.nombre=v_nomproducto
        buscado.stock=v_stockproducto
        buscado.precio=v_preproducto

        Producto.save(buscado)
        return redirect('/')
<<<<<<< HEAD
>>>>>>> 2f6b4c37de69e19b2f9d2c3f3db22fa8dbc8c572
=======
>>>>>>> Juan
