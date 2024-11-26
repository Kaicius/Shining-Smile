# Generated by Django 5.1.3 on 2024-11-12 14:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_perfil'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='especialidade',
            name='medicos',
            field=models.ManyToManyField(related_name='especialidades', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='especialidade',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]