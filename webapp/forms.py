from django import forms
from django.forms import extras

from django.contrib.auth.models import User

class NameForm(forms.Form):
	
	name = forms.CharField(widget=forms.TextInput(), label='Nome', max_length=200)
	sname = forms.CharField(widget=forms.TextInput(), label='Sobrenome', max_length=200)
	age = forms.DateField(widget=extras.SelectDateWidget(years = range(2022, 1930, -1)))
	address = forms.CharField(widget=forms.TextInput(), label='Endereco', max_length=200)	
	city = forms.CharField(widget=forms.TextInput(), label='Cidade', max_length=200)	
	state1 = forms.CharField(widget=forms.TextInput(), label='Estado', max_length=200)	
	country = forms.CharField(widget=forms.TextInput(), label='Pais', max_length=200)	
	email = forms.CharField(widget=forms.EmailInput(), label='Email', max_length=200)		
	password1 = forms.CharField(widget=forms.PasswordInput(), label='Senha', max_length=200)	
	password2 = forms.CharField(widget=forms.PasswordInput(), label='Senha Novamente', max_length=200)

	class Meta:
		model = User

class Login(forms.Form):

	email = forms.CharField(widget=forms.EmailInput(), label='Email', max_length=200)		
	password = forms.CharField(widget=forms.PasswordInput(), label='Senha', max_length=200)	

class AccForm(forms.Form):

	MY_CHOICES = (
    ('1', 'Conta Banco'),
    ('2', 'Cartao de Credito'),
    ('3', 'Conta de agua'),
    ('4', 'Conta de luz'),
    ('5', 'Conta de telefone'),
	('6', 'Conta de aluguel'),
	('7', 'Gastos alimentacao'),
	('8', 'Gastos Diversao'),
	('9', 'Gastos Viagens'),
	('10', 'Outros'),
	)

	MY_MONTHS = (
    ('1', 'Janeiro'),
    ('2', 'Fevereiro'),
    ('3', 'Marco'),
    ('4', 'Abril'),
    ('5', 'Maio'),
	('6', 'Junho'),
	('7', 'Julho'),
	('8', 'Agosto'),
	('9', 'Setembro'),
	('10', 'Outubro'),
	('11', 'Novembro'),
	('12', 'Dezembro'),
	)


	bill_type = forms.ChoiceField(choices=MY_CHOICES, label='Tipo de Conta')
	bill_desc = forms.CharField(widget=forms.TextInput(), label='Identificador', max_length=200)  # Criar no Model
	bill_mont = forms.ChoiceField(choices=MY_MONTHS, label='Mes')
	bill_recu = forms.BooleanField(widget=forms.CheckboxInput(), label='Recorrente?')  # Criar no Model
	bill_cost = forms.FloatField(widget=forms.NumberInput(), label='Valor:')
	bill_date = forms.DateField(widget=extras.SelectDateWidget(years = range(2022, 2000, -1)), label="Data de Expiracao")
	# Criar no model
	#bill_date_add = Only in database
	bill_share_email = forms.CharField(widget=forms.EmailInput(), label='Agregado Email (opcional)', max_length=200)		
	bill_share_name = forms.CharField(widget=forms.TextInput(), label='Agregado Nome (opcional)', max_length=200)

