numero1 = int(input("Digite primeiro numero: "))
numero2 = int(input("Digite segundo numero: "))
parOuImpar = (numero1 + numero2) % 2

if(parOuImpar == 0):
    parOuImpar = "O numero é par"
else: parOuImpar = "O numero e impar"

print(parOuImpar)