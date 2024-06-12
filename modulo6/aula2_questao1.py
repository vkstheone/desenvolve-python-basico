import random

valores = []
for i in range(20):
    numeros=random.randint(-100,100)
    valores.append(numeros)

print(sorted(valores))
print(valores)
#posição do maior valor
print(valores.index(max(valores))) 
# do menor valorposição
print(valores.index(min(valores))) 
