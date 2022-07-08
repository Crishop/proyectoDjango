from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def inventario(request):
    return render(request,'inventario.html')

def home(request):
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
