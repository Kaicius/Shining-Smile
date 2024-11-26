from django.db import models
from django.contrib.auth.models import User

class Consulta(models.Model):
    paciente = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='consultas_paciente',  # Nome único do paciente
        related_query_name='consulta_paciente',  # Nome único na consulta do paciente
        limit_choices_to={'groups__name': 'Paciente'}
    )
    
    medico = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='consultas_medico',  # Nome único do medico
        related_query_name='consulta_medico',  # Nome único na consulta do medico
        limit_choices_to={'groups__name': 'Médico'}
    )
    
    dia_da_consulta = models.DateField()
    hora = models.TimeField()
    
    status = models.CharField(
        max_length=20, 
        choices=[
            ('confirmada', 'Confirmada'),
            ('cancelada', 'Cancelada'),
            ('pendente', 'Pendente')
        ], 
        default='pendente'
    )

    def __str__(self):
        return f"Consulta {self.id} - {self.paciente} com {self.medico} em {self.dia_da_consulta} às {self.hora}"

    class Meta:
        ordering = ['dia_da_consulta', 'hora']
