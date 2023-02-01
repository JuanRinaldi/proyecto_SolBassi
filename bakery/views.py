from django.shortcuts import render 
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from .forms import RegisterForm
from productos.models import Product

def index(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'index.html', {
        'message': 'Listados de productos',
        'products': products,
    })


def login_view (request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST': #para traer lo agregado en el formulario
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #autenticamos y generamos usuario de no estar registrado
        user = authenticate(username=username , password=password)
        if user:
            login(request, user)
            messages.success(request, "Bienvenido {}".format(user.username))
            return redirect('index')
        else:
            messages.error(request, "Usuario o contraseña no validos")
            
    return render(request, 'login.html' ,{
        
    })


def logout_view(request):
    logout(request)
    messages.success(request, 'sesión cerrada con exito')
    return redirect('login')

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Creado exitosamente')
            return redirect('index')
    
    return render(request, 'register.html', {
        'form':form
    })
