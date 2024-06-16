import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    
    nomes_criptografados = []
    for nome in nomes:
        criptografado = ""
        for char in nome:
            novo_codigo = 33 + (ord(char) + chave_aleatoria - 33) % 94
            criptografado += chr(novo_codigo)
        nomes_criptografados.append(criptografado)
    
    return nomes_criptografados, chave_aleatoria

# Exemplo de uso
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print("Chave de criptografia:", chave)
print("Nomes criptografados:", nomes_criptografados)