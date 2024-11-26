from django.contrib.auth.models import Group
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def add_user_to_paciente_group(request, user, **kwargs):
    """
    Adiciona automaticamente um novo usuário ao grupo 'Paciente'
    após o cadastro bem-sucedido no Django Allauth.
    """
    # Obtém o grupo 'Paciente' (certifique-se de que ele já exista)
    group, created = Group.objects.get_or_create(name='Paciente')
    
    # Adiciona o usuário ao grupo
    user.groups.add(group)
