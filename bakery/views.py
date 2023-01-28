from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages

def index(request):
    return render(request, 'index.html', {
        
    })


def view_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username , password= password)
        if user:
            login(request, user)
            messages.success(request, "bienvenido {}".format(user.username))
            return redirect('index')
        else:
            messages.error(request, "Usuario y/o contraseña no validos")

    return render(request, 'login.html' , {

    })




def view_logout():
    pass

def registro():

    pass


