import random
import math

quantidade = int(input('Quantos valores? '))
soma= 0

for i in range(quantidade):
    valores=random.randint(0, 100)
    print(valores)
    soma += valores

print(f'A soma destes {quantidade} valores aleatórios é:',soma)
print(f'E a raiz quadrada de {soma} é {math.sqrt(soma):.2f}')