Website
Language:Django + bootstrap + sqlite/postgree

Scheme:
	Login;
			Spreadsheet Map		(Daily, Monthly, Anual)
			Users(Depedents)	(Add/remove/edit User)
			bill				(Add/remove/edit, Add/edit/remove bill, )
			Bank Account		(Add/remove/edit, Add/edit/remove bill, )
			Historic			(history)



DB Schema

Users:	name(var 30), sname(var30), age(datefield), address(var 30), city(var 15), country(var 10), email(varchar 30), password(var 15)
		
Bill:  billtype(var 15), vcost(int 12),  expirateDate(datefield), status(boolean), recurrency(boolean), FK_users_email, FK_billshare_dependent

BillShare: dependent(varchar 15), email(varchar 30), FK_users_email, 

Criar telas:
			1 Adicao de contas em geral
					Adicionar valores a conta

			2 Adicao de cartao de credito
					Adiconar valores ao cartao

			3 Criar profile Usuario
					Visualizacao e edicao

			4 Criar acesso somente autenticado		





WebMobile


App Android