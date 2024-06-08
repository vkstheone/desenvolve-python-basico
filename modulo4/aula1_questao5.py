n = int(input(""))

soma = 0
cont = 0

while cont < n:
    idade = int(input())
    soma += idade
    cont += 1

print(soma)
print(f"A média das idades é {soma/n:.0f}")