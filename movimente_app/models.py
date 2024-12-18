from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Jogador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apelido = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=10, default='ativo')
    data_criacao = models.DateTimeField(default=timezone.now)
    ultimo_acesso = models.DateTimeField(default=timezone.now)
    pontuacao_total = models.IntegerField(default=0)
    
    def __str__(self):
        return self.apelido


class Jornada(models.Model):
    ESTADOS = [
        ('ativa', 'Ativa'),
        ('inativa', 'Inativa'),
    ]

    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='jornadas')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    estado_atual = models.CharField(max_length=8, choices=ESTADOS, default='ativa')
    progresso_na_jornada = models.FloatField(default=0.0)  # progresso inicial de 0
    codigo = models.CharField(max_length=200, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = f'{self.jogador.apelido}_{self.id}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
    

# apenas para simulacao
class Premio(models.Model):
    tipo = models.CharField(max_length=255)
    data_aquisicao = models.DateTimeField()
    
    def __str__(self):
        return f'{self.tipo} - {self.data_aquisicao}'