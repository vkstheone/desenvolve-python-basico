def calcular(cpf, posicoes):
    soma = 0
    for i, multiplicador in enumerate(range(posicoes + 1, 1, -1)):
        soma += int(cpf[i]) * multiplicador
    resto = soma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    primeiro_digito = calcular(cpf, 9)
    
    segundo_digito = calcular(cpf[:9] + str(primeiro_digito), 10)
    
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"

cpf_usuario = input("Digite um CPF na forma XXX.XXX.XXX-XX: ")

if validar_cpf(cpf_usuario):
    print("Válido")
else:
    print("Inválido")