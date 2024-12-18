from django import forms
from django.contrib.auth.models import User
from .models import Jogador, Jornada
from django.utils import timezone

class JogadorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Adicionando um campo de senha

    class Meta:
        model = Jogador
        fields = ['apelido', 'nome', 'email', 'password']

    def save(self, commit=True):
        jogador = super().save(commit=False)
        if commit:
            user = User.objects.create_user(
                username=jogador.apelido,
                password=self.cleaned_data['password']  # Criando o usuário com senha
            )
            jogador.user = user
            jogador.status = 'ativo'
            jogador.data_criacao = timezone.now()
            jogador.ultimo_acesso = timezone.now()
            jogador.pontuacao_total = 0
            jogador.save()
        return jogador


class JornadaForm(forms.ModelForm):
    class Meta:
        model = Jornada
        fields = ['nome', 'descricao']
