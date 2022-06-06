from django.shortcuts import render

# Create your views here.
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
