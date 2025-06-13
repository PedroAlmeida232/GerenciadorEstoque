import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerenciador_estoque.settings')
django.setup()

from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

def setup_groups():
    # Criar grupos
    usuarios_group, _ = Group.objects.get_or_create(name='Usuarios')
    gerentes_group, _ = Group.objects.get_or_create(name='Gerentes')
    superiores_group, _ = Group.objects.get_or_create(name='Superiores')

    # Criar usuário padrão
    if not User.objects.filter(username='usuario').exists():
        usuario = User.objects.create(
            username='usuario',
            password=make_password('usuario123'),
            is_staff=True
        )
        usuario.groups.add(usuarios_group)

    # Criar gerente
    if not User.objects.filter(username='gerente').exists():
        gerente = User.objects.create(
            username='gerente',
            password=make_password('gerente123'),
            is_staff=True
        )
        gerente.groups.add(gerentes_group)

    # Criar superior
    if not User.objects.filter(username='superior').exists():
        superior = User.objects.create(
            username='superior',
            password=make_password('superior123'),
            is_staff=True
        )
        superior.groups.add(superiores_group)

    # Criar superusuário
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )

if __name__ == '__main__':
    setup_groups()
    print("Configuração concluída com sucesso!") 