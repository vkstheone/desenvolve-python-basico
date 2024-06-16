def sao_anagramas(palavra1, palavra2):
    return sorted(palavra1.lower()) == sorted(palavra2.lower())

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

anagramas = []

palavras = frase.split()

for palavra in palavras:
    if sao_anagramas(palavra, palavra_objetivo):
        anagramas.append(palavra)

print("Anagramas:", anagramas)