from django.db import models

class Usuario(models.Model):
	first_name = models.CharField(max_length=50,blank=True)
	last_name = models.CharField(max_length=50,blank=True)
	age = models.DateField()
	user_create_date = models.DateField(auto_now_add=True)
	address = models.CharField(max_length=100,blank=True)
	country = models.CharField(max_length=100,blank=True)
	state = models.CharField(max_length=100, blank=True,default="")
	city = models.CharField(max_length=100,blank=True)
	email = models.EmailField(max_length=100) 
	password = models.CharField(max_length=12,blank=True)


	def __str__(self):
		return "{0} {1} {2} {3} {4} {5} {6} {7}".format(self, self.first_name, self.last_name, self.address, self.country, self.estate, self.city, self.email, self.password)

class UsuarioTeste(models.Model):
	nome = models.CharField(max_length=100)
	
	def __str__(self):
		return "{0} {1}".format(self, self.nome)


class Conta(models.Model):
	usuarioID = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	bill_type = models.CharField(max_length=100)
	bill_cost = models.FloatField()
	bill_date = models.DateField()
	bill_desc = models.CharField(max_length=100,null=True)
	bill_create_date = models.DateField(auto_now_add=True, blank=True, null=True)

class Dependente(models.Model):
	usuarioID = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	email =	models.EmailField(max_length=100)

class DependenteConta(models.Model):
	contaID = models.ForeignKey(Conta, on_delete=models.CASCADE)
	dependenteID = models.ForeignKey(Dependente, on_delete=models.CASCADE)