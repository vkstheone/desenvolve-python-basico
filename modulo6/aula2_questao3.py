import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

#lista de intersecção sem duplicatas
interseccao = sorted(list(set(lista1) & set(lista2)))

# Função para contar ocorrências de elementos em uma lista

def contar_ocorrencias(lista):
    contagem = {}
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    return contagem

contagem_lista1 = contar_ocorrencias(lista1)
contagem_lista2 = contar_ocorrencias(lista2)

print("lista1 -", lista1)
print("lista2 -", lista2)


print("Interseccao -", interseccao)



# Imprime a contagem de cada elemento na intersecção
print("Contagem")
for elemento in interseccao:
    print(f"{elemento}: (lista1={contagem_lista1.get(elemento, 0)}, lista2={contagem_lista2.get(elemento, 0)})")