meses = ["Janeiro", "Fevereiro", "Março", 
         "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro",
         "Outubro", "Novembro", "Dezembro"]

data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

dia, mes, ano = data_nascimento.split('/')

dia = int(dia)
mes = int(mes)
ano = int(ano)

nome_mes = meses[mes - 1]

print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")