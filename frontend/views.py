from django.shortcuts import render, redirect
from urllib import response
from django.http import HttpResponse
from .models import Usuario

# Create your views here.
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
