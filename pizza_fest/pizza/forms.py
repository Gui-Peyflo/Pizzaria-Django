from django.forms import ModelForm

from .models import Endereco, Usuario, Borda



class enderecoForm(ModelForm):
   class Meta:
       model = Endereco
       fields = ['logradouro', 'endereco', 'bairro','municipio','estado','numero']


class usuarioForm(ModelForm):
   class Meta:
       model = Usuario
       fields = ['nome', 'senha', 'cpf', 'email', 'telefone', 'idEndereco']













