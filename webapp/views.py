from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from .forms import NameForm, Login, AccForm
from .models import Usuario

from django.contrib.auth import authenticate, login as auth_login

from django.contrib.auth import logout
from django.contrib.auth.models import User

def index(request):
	if not request.user.is_authenticated():
		return redirect('/login')

	for a in Usuario.objects.all():
		if a.email == 'teste2@teste.com':
		 print(a.first_name) # this is the address that SQL brought in via a "join".	
	#query = Usuario()
	#print(query.objects.get('first_name'))	
	return render(request, 'webapp/index.html', {'form': a.first_name})

def accounts(request):
	
	if not request.user.is_authenticated():
		return redirect('/login') 

	if request.method == 'POST':
		
		form = AccForm(request.POST)

		if form.is_valid():
			fc = form.cleaned_data
			#db_save = Usuario(first_name = fc.get('name'), last_name = fc.get('sname'), age = fc.get('age'),address = fc.get('address'), state = fc.get('state1'), city = fc.get('city'), country = fc.get('country'), email = fc.get('email'), password = fc.get('password1') )
			#db_save.save()

			return redirect('/account')
	else:
		form = AccForm()

	return render(request, 'webapp/accounts.html', {'form': form})	
	

def users(request):

	if not request.user.is_authenticated():
		return redirect('/login') 

	return render(request, 'webapp/users.html')

def hist(request):

	if not request.user.is_authenticated():
		return redirect('/login') 

	return render(request, 'webapp/hist.html')

def cadastro(request):	
	return render(request, 'webapp/cadastro.html')

def cadastro_done(request):	
	return render(request, 'webapp/cadastro_done.html')	

def login(request):
	form = Login()

	if request.method == "POST":
		
		#form = Login(request.POST)	
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				
				return render(request, 'webapp/index.html')
			else:

				return render(request, 'webapp/login.html', {'error': 'Conta Desabilitada', 'form': form})
		else:
			return render(request, 'webapp/login.html', {'error': 'Login Invalido!', 'form': form})
		
			
	return render(request, 'webapp/login.html', {'form': form})

def logout_user(request):
	logout(request)
	#form = Login(request.POST or None)
	return redirect('/login')
	#return render(request, 'webapp/login.html', {'form': form})


def cadastro_proc(request):
    # if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST or None)

		#print(form)
		if form.is_valid():
			
			#CLeaned Data
			fc = form.cleaned_data
			username = fc.get('email')
			password = fc.get('password1')
			#print(city)

			#DB save
			db_save = Usuario(first_name = fc.get('name'), last_name = fc.get('sname'), age = fc.get('age'),address = fc.get('address'), state = fc.get('state1'), city = fc.get('city'), country = fc.get('country'), email = fc.get('email'), password = fc.get('password1') )
			db_save.save()

			#Django Admin login/session save
			user = User.objects.create_user(username, email=username, password=password)
			## first_name, last_name (createuser)
			#user = form.save(commit=False)
			#user.set_password(password)
			user.save()

			html = "<html><meta http-equiv='Refresh' content='5;url=/login'><body>Cadastro Concluido!.</body></html>"
			return HttpResponse(html)
				
		
			
			#utilizar
			#return redirect('index')
	else:
		form = NameForm()

	return render(request, 'webapp/cadastro.html', {'form': form})




