from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from pedidos.forms import CustomLoginForm, CustomUserCreationForm
from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    return render(request, 'home.html')
def user(request):
    return render(request, 'user.html')

def blank(request):
    return render(request, 'blank.html')

#def asignar_mesa(request):
     #cliente.asignar_mesa()


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user')  # Cambia la URL según tu necesidad
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardamos el nuevo usuario
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('login')  # Redirige a una página después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})