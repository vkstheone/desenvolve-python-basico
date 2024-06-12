def ler_lista(nome_lista):
    quantidade = int(input(f"Digite a quantidade de elementos da {nome_lista}: "))
    lista = []
    print(f"Digite os {quantidade} elementos da {nome_lista}:")
    for _ in range(quantidade):
        elemento = int(input())
        lista.append(elemento)
    return lista

# Função para intercalar duas listas
def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    len_lista1 = len(lista1)
    len_lista2 = len(lista2)
    min_len = min(len_lista1, len_lista2)
    
    for i in range(min_len):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    
    if len_lista1 > len_lista2:
        lista_intercalada.extend(lista1[min_len:])
    else:
        lista_intercalada.extend(lista2[min_len:])
    
    return lista_intercalada

lista1 = ler_lista("lista 1")
lista2 = ler_lista("lista 2")


lista_intercalada = intercalar_listas(lista1, lista2)

print("Lista intercalada:", lista_intercalada)