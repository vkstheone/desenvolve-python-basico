import random


def embaralhar_palavras(frase):
    palavras = frase.split()

    palavras_embaralhadas = []

    for palavra in palavras:
    
        if len(palavra) < 4:
            palavras_embaralhadas.append(palavra)
        else:
            letras_interiores = list(palavra[1:-1])
            random.shuffle(letras_interiores)
            palavra_embaralhada = palavra[0] + ''.join(letras_interiores) + palavra[-1]
            palavras_embaralhadas.append(palavra_embaralhada)

    frase_embaralhada = ' '.join(palavras_embaralhadas)
    return frase_embaralhada


frase = input("Digite a frase que deseja embaralhar: ")
resultado = embaralhar_palavras(frase)
print("Frase embaralhada:", resultado)