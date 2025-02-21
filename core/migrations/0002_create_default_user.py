from django.contrib.auth.models import User
from django.db import migrations

def create_default_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Staff = apps.get_model('core', 'Staff')  # Reemplaza "core" por el nombre de tu app
    
    if not User.objects.filter(username="rroncancio").exists():
        user = User.objects.create_user(username="rroncancio", email="usuario1@example.com", password="E.987321")
        Staff.objects.create(user=user, phone="123456789", image="")
        print("Usuario básico creado: usuario1")

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_user),
    ]
