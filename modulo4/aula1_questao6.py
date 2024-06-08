n= int(input('Digite a quantidade de experimentos: '))
cont= 0
soma_sapo, soma_rato, soma_coelho= 0,0,0

while cont < n:
    quantia= int(input('Quantos: '))
    tipo= (input('Qual o tipo: '))

    if tipo== 'S': 
        soma_sapo += quantia
    elif tipo== 'R':
        soma_rato += quantia
    elif tipo== 'C':
        soma_coelho += quantia
    
    cont +=1

Total_de_cobaias= soma_sapo+soma_rato+soma_coelho
print('Total de cobaias: ',Total_de_cobaias)
print('Total de sapos: ',soma_sapo)
print('Total de ratos: ',soma_rato)
print('Total de coelhos: ',soma_coelho)

print("Percentual de sapos:", (soma_sapo/Total_de_cobaias) * 100)
print("Percentual de ratos:", (soma_rato/Total_de_cobaias) * 100)
print("Percentual de coelhos:", (soma_coelho/Total_de_cobaias) *100)