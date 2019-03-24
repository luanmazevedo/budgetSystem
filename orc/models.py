from django.db import models

# Create your models here.

class IdentificadorCartao(models.Model):
	CREDITO = 'cred'
	DEBITO = 'deb'
	TIPO_CARTAO_CHOICE = (
		(CREDITO, 'Cartão de Crédito'),
		(DEBITO, 'Cartão de Débito'),
	)
	tipo_cartao = models.CharField(
		max_length=4,
		choices=TIPO_CARTAO_CHOICE,
	)
	nome_cartao = models.CharField(max_length=50)
	dono_cartao = models.ForeignKey('auth.User', on_delete=models.CASCADE)
