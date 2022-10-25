from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CrearUsuarioForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):

    if request.method == 'GET':
        return render(request, './signup.html', {'form': CrearUsuarioForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password2'], first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'], email=request.POST['email']
                )
                user.save()
                login(request, user)
                return redirect('index')
            except:
                return render(request, 'signup.html', {'form': CrearUsuarioForm, 'error': 'Error del Procesado'})
        else:
            return render(request, 'signup.html', {'form': CrearUsuarioForm, 'error': 'Contraseñas no coinciden'})


@login_required
def signout(request):
    logout(request)
    return redirect('login')


def signin(request):
    if request.method == 'GET':
        form = AuthenticationForm
        return render(request, 'signin.html', {'form': form})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            form = AuthenticationForm
            return render(request, 'signin.html', {'form': form, 'error': 'Usario o Clave Incorrecta!'})
        else:
            login(request, user)
            return redirect('index')
