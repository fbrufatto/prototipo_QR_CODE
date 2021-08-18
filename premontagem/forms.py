from django.forms import ModelForm

from premontagem.models import Bike

class AddBicicletaForm(ModelForm):
    class Meta:
        model = Bike
        fields = [
            'ordem',
            'marca',
            'modelo',
            'genero',
            'tamanho',
            'nquadro',
            'nmotor',
            'ndisplay',
            'ncontrolador',
            'nbateria',
            'linha',
            'travaofrente',
            'travaotras',
            'mudanca',
            #'imagem',
            'descricao',

        ]