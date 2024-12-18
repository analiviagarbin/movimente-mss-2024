from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import JogadorForm, JornadaForm
from .models import Jogador, Jornada
from django.contrib import messages


# Jogador

# Listar todos
def jogador_list(request):
    jogadores = Jogador.objects.all()
    return render(request, 'jogador/listar.html', {'jogadores': jogadores})


# Registrar novo jogador
def jogador_register(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jogador_login')
    else:
        form = JogadorForm()
    return render(request, 'jogador/registrar.html', {'form': form})


# Login
def jogador_login(request):
    if request.method == 'POST':
        apelido = request.POST['apelido']
        password = request.POST['password']

        try:
            jogador = Jogador.objects.get(apelido=apelido)

            # Usa o modelo User para autenticar
            user = authenticate(request, username=jogador.user.username, password=password)
            
            if user is not None:
                login(request, user)
                jogador.ultimo_acesso = timezone.now()
                jogador.save()
                return redirect('menu')  # Redireciona para o menu
            else:
                messages.error(request, 'Senha incorreta.')
        except Jogador.DoesNotExist:
            messages.error(request, 'Jogador não encontrado.')

    return render(request, 'jogador/login.html')


# Logout
@login_required
def jogador_logout(request):
    logout(request)
    return redirect('jogador_login')


# Menu
@login_required
def menu(request):
    return render(request, 'jogador/menu.html')



# Jornada

# Listar jornadas
@login_required
def listar_jornadas(request):
    jogador = Jogador.objects.get(user=request.user)
    jornadas = Jornada.objects.filter(jogador=jogador)
    return render(request, 'jornada/listar_jornadas.html', {'jornadas': jornadas})


# Criar nova jornada
@login_required
def criar_jornada(request):
    jogador = Jogador.objects.get(user=request.user)
    if request.method == "POST":
        form = JornadaForm(request.POST)
        if form.is_valid():
            jornada = form.save(commit=False)
            jornada.jogador = jogador
            jornada.save()
            return redirect('listar_jornadas')
    else:
        form = JornadaForm()
    
    return render(request, 'jornada/criar.html', {'form': form})