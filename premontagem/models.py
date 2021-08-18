from io import BytesIO
from django.db import models


# Create your models here.

class Bike(models.Model):
    LINHA_CHOICES = [
        ('L1', 'Linha 1'),
        ('L2', 'Linha 2'),
    ]

    GEN = [
        ('M', 'M'),
        ('F', 'F'),
    ]

    SIZE = [
        ('44', '44'),
        ('46', '46'),
        ('49', '49'),
        ('53', '53'),
        ('54', '54'),
        ('58', '58'),
    ]

    TRAVAOFRENTE = [
        ('1', 'OK'),
        ('2', 'Desafinado'),
        ('3', 'Não Feito'),
    ]

    TRAVAOTRAS = [
        ('1', 'OK'),
        ('2', 'Desafinado'),
        ('3', 'Não Feito'),
    ]

    MUDANCA = [
        ('1', 'OK'),
        ('2', 'Desafinado'),
        ('3', 'Não Feito'),
    ]


    ordem = models.CharField('Número da Ordem', max_length=50, blank=True)
    marca = models.CharField('Marca', max_length=50, blank=True)
    modelo = models.CharField('Modelo', max_length=50, blank=True)
    genero = models.CharField('Gênero', max_length=2, choices=GEN)
    tamanho = models.CharField('Tamanho', max_length=2, choices=SIZE)
    nquadro = models.CharField('Número do Quadro', max_length=50, blank=True, primary_key=True)
    nmotor = models.CharField('Número do Motor', max_length=50, blank=True)
    ndisplay = models.CharField('Número Display', max_length=50, blank=True)
    ncontrolador = models.CharField('Número do Controlador', max_length=50, blank=True)
    nbateria = models.CharField('Número da Bateria', max_length=50, blank=True)
    linha = models.CharField('Linha de Montagem', max_length=2, choices=LINHA_CHOICES)
    travaofrente = models.CharField('Travão Frente: ', max_length=2, choices=TRAVAOFRENTE)
    travaotras = models.CharField('Travão Tras: ', max_length=2, choices=TRAVAOTRAS)
    mudanca = models.CharField('Mudança: ', max_length=2, choices=MUDANCA)
   # imagem = models.ImageField('Imagem do defeito', null=True)
    descricao = models.TextField('Descrição do defeito', blank=True)

    def __str__(self):
        return str(self.nquadro)


