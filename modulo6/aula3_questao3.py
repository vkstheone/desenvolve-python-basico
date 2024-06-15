import random
lista = [random.randint(-10, 10) for _ in range(20)]

print("Original:", lista)

max_negativos = 0
best_interval = (0, 0)

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        sub_lista = lista[i:j]
        count_negativos = sum(1 for x in sub_lista if x < 0)
        if count_negativos > max_negativos:
            max_negativos = count_negativos
            best_interval = (i, j)

del lista[best_interval[0]:best_interval[1]]

print("Editada:", lista)