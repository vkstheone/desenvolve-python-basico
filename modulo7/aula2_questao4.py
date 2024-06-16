def validador_senha(senha):
    caracteres_especiais = '!@#$%^&*()_+|:"<>?`-=[];,./{}'

    if len(senha) < 8:
        return False
    if not any(char.isupper() for char in senha) or not any(char.islower() for char in senha):
        return False
    if not any(char.isdigit() for char in senha):
        return False
    if not any(char in caracteres_especiais for char in senha):
        return False
    return True

senha = input("Digite a senha: ")

if validador_senha(senha): print("Senha válida!")
else: print("Senha inválida!")