distancia = int(input("Digite a disctancia: "))
peso = int(input("Digite a distancia: "))
valor = 0

if(distancia <= 100): valor = peso * 1
if(distancia >= 101 and distancia <= 300): valor = peso * 1.50
if(distancia >  300): valor = peso * 2
if(peso > 10): valor = valor + 10

print(f"O valor do frete é R${valor:.2f}")
