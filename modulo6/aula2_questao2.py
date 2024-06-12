import random

num_elementos= random.randint(5,20) 
print('Número de elementos:',num_elementos)

elementos= []
for i in range(num_elementos):
    sorteio=random.randint(1,10)
    elementos.append(sorteio)

print(elementos)
print('Soma dos valores:',sum(elementos))
print('Média dos valores:',sum(elementos)/len(elementos))