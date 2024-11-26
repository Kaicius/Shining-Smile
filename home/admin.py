from django.contrib import admin
from .models import Consulta

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'dia_da_consulta', 'hora', 'status')  # Corrigido 'horario' para 'hora'
    search_fields = ('paciente__username', 'medico__username')  # Exemplo de como buscar pelo nome do paciente ou médico

admin.site.register(Consulta, ConsultaAdmin)
