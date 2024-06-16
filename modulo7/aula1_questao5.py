frase = input("Digite uma frase: ")

contador_vogais = 0
indices_vogais = []

indice = 0
for caractere in frase:
    if caractere.lower() in "aeiou":
        contador_vogais += 1
        indices_vogais.append(indice)
    indice += 1

print(f"{contador_vogais} vogais")
print("Índices", indices_vogais)