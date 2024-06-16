frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

frase_modificada = ""

for char in frase:
    if char in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += char

print("Frase modificada:", frase_modificada)