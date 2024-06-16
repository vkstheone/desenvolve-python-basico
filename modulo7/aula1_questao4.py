numero = input("Digite o número: ")

if len(numero) == 8:
    numero = '9' + numero
elif len(numero) == 9:
    if numero[0] == '9':
        print("O número começa com o dígito 9. ")
    

numero_formatado = numero[:5] + '-' + numero[5:]

print("Número completo:", numero_formatado)