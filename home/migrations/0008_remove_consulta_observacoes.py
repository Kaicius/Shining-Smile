# Generated by Django 5.1.3 on 2024-11-18 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_consulta_observacoes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='observacoes',
        ),
    ]
