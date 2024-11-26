from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils import timezone
from datetime import timedelta, datetime
from django.contrib.auth.models import Group
from .models import Consulta, User
from .forms import MedicoCreationForm
import random
import string
from django.contrib import messages

# Função para verificar se o usuário é administrador
def is_admin(user):
    return user.is_staff

# Função para verificar se o usuário é médico
def is_medico(user):
    return user.groups.filter(name='Médico').exists()

# Função para verificar se o usuário é paciente
def is_paciente(user):
    return user.groups.filter(name='Paciente').exists()

# Página inicial
def home_views(request):
    return render(request, 'home.html')

def homelogado_views(request):
    return render(request, 'home_logado.html')

# Se o usuário for paciente, ele pode ver suas consultas
@login_required
def minhas_consultas(request):
    consultas = Consulta.objects.filter(paciente=request.user)
    return render(request, 'minhas_consultas.html', {'consultas': consultas})

# Página do dashboard do administrador
@user_passes_test(is_admin, login_url='admin_login')
def admin_dashboard(request):
    today = timezone.now()
    consultas = Consulta.objects.all()
    users_last_24h = User.objects.filter(last_login__gte=today - timedelta(hours=24))
    medicos_last_24h = users_last_24h.filter(groups__name='Médico')
    admins_last_24h = users_last_24h.filter(is_staff=True)

    consultas_por_medico = {}
    for consulta in consultas:
        medico = consulta.medico  # Acesso ao médico
        nome_completo = f"{medico.first_name} {medico.last_name}"  # Concatenando o primeiro e o último nome
        if nome_completo not in consultas_por_medico:
            consultas_por_medico[nome_completo] = []  # Usando nome completo como chave
        consultas_por_medico[nome_completo].append(consulta)  # Adicionando a consulta ao médico

    context = {
        'consultas': consultas,
        'users_last_24h': users_last_24h.count(),
        'medicos_last_24h': medicos_last_24h.count(),
        'admins_last_24h': admins_last_24h.count(),
        'consultas_por_medico': consultas_por_medico,  # Agora o dicionário tem o nome completo como chave
    }
    return render(request, 'adm.html', context)



# Página de login de administrador
def admin_login(request):
    if request.user.is_authenticated:
        if is_admin(request.user):
            return redirect('admin_dashboard')  # Redireciona se o usuário for admin
        else:
            error = "Você não tem permissão para acessar esta área."
            return redirect('home')  # Redireciona para a página inicial

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and is_admin(user):
            login(request, user)
            return redirect('admin_dashboard')
        else:
            error = "Credenciais inválidas ou você não tem acesso de administrador."
            return render(request, 'adm_login.html', {'error': error})

    return render(request, 'adm_login.html')

#Pagina login de Medico
def medico_login(request):
    if request.user.is_authenticated:
        if is_medico(request.user):
            return redirect('minhas_consultas')  # Redireciona se o usuário for médico
        else:
            messages.error(request, "Você não tem permissão para acessar esta área.")
            return redirect('home')  # Redireciona para a página inicial ou outra página

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and is_medico(user):
            login(request, user)
            return redirect('medico_home')  # Página de consultas do médico
        else:
            messages.error(request, "Credenciais inválidas ou você não tem acesso de médico.")
            return render(request, 'medico_login.html')  # Retorna à página de login de médico

    return render(request, 'medico_login.html')

#Home medico
@login_required
def medico_home(request):
    medico = request.user  # Supomos que o médico está logado
    consultas_agendadas = Consulta.objects.filter(medico=medico, dia_da_consulta__gte=timezone.now()).count()

    # Obter consultas futuras ou atuais
    consultas = Consulta.objects.filter(medico=medico, dia_da_consulta__gte=timezone.now())

    context = {
        'consultas_agendadas': consultas_agendadas,
        'consultas': consultas,
    }
    return render(request, 'medico.html', context)


# Função para gerar username aleatório para medico
def generate_random_username(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Página para adicionar médico
@user_passes_test(is_admin, login_url='admin_login')
def add_medico(request):
    if request.method == 'POST':
        form = MedicoCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = generate_random_username()  # Gera o username automaticamente
            user.set_password(form.cleaned_data['password1'])  # Usa password1 como senha
            user.is_staff = False
            user.save()
            # Adiciona o usuário ao grupo "Médico"
            group, created = Group.objects.get_or_create(name='Médico')
            user.groups.add(group)
            return redirect('gerenciar_medicos')
    else:
        form = MedicoCreationForm()
    return render(request, 'add_medico.html', {'form': form})

# Página para gerenciar médicos
@user_passes_test(is_admin, login_url='admin_login')
def gerenciar_medicos(request):
    medicos = User.objects.filter(groups__name='Médico')
    return render(request, 'gerenciar_medicos.html', {'medicos': medicos})

# Página para remover médico
@user_passes_test(is_admin, login_url='admin_login')
def remover_medico(request, medico_id):
    medico = get_object_or_404(User, id=medico_id)
    if medico.groups.filter(name='Médico').exists():
        medico.delete()
    return redirect('gerenciar_medicos')

# Página para resetar a senha do médico
@user_passes_test(is_admin, login_url='admin_login')
def resetar_senha_medico(request, medico_id):
    medico = get_object_or_404(User, id=medico_id, groups__name='Médico')
    if request.method == 'POST':
        nova_senha = request.POST.get('nova_senha')
        if nova_senha:
            medico.set_password(nova_senha)
            medico.save()
            return render(request, 'senha_resetada.html', {'medico': medico, 'nova_senha': nova_senha})
    return render(request, 'resetar_senha.html', {'medico': medico})


#Agendar consulta
@login_required
def agendar_consulta(request):
    if request.method == 'POST':
        medico_id = request.POST.get('medico')
        dia_da_consulta = request.POST.get('dia_da_consulta')
        hora = request.POST.get('hora')
        
        # Convertendo a data e hora
        dia_da_consulta = datetime.strptime(dia_da_consulta, '%Y-%m-%d').date()
        hora = datetime.strptime(hora, '%H:%M').time()

        # Verificando se a consulta já existe
        if Consulta.objects.filter(medico_id=medico_id, dia_da_consulta=dia_da_consulta, hora=hora).exists():
            # Exibir mensagem de erro se já houver uma consulta no mesmo horário
            return render(request, 'agendar_consulta.html', {'error': 'Já existe uma consulta nesse horário.'})

        # Criar a nova consulta
        consulta = Consulta.objects.create(
            paciente=request.user,
            medico_id=medico_id,
            dia_da_consulta=dia_da_consulta,
            hora=hora,
            status='pendente'
        )
        
        return redirect('minhas_consultas')  # Redireciona para a lista de consultas agendadas do paciente

    medicos = User.objects.filter(groups__name='Médico')  # Lista de médicos disponíveis
    # Passando o nome completo do médico para o template
    medicos = [(medico.id, f"{medico.first_name} {medico.last_name}") for medico in medicos]

    return render(request, 'agendar_consulta.html', {'medicos': medicos})


@login_required
def minhas_consultas(request):
    consultas = Consulta.objects.filter(paciente=request.user)
    return render(request, 'minhas_consultas.html', {'consultas': consultas})