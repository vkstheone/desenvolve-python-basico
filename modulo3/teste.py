## Não altere os atributos definidos a seguir
iris1_a1, iris1_a2, iris1_a3 = 123, 456, 789
iris2_a1, iris2_a2, iris2_a3 = 987, 654, 321
iris3_a1, iris3_a2, iris3_a3 = 111, 222, 333
iris4_a1, iris4_a2, iris4_a3 = 444, 555, 666

## Escreva e execute seu código aqui

usuarios = {
    1: (iris1_a1, iris1_a2, iris1_a3),
    2: (iris2_a1, iris2_a2, iris2_a3),
    3: (iris3_a1, iris3_a2, iris3_a3),
    4: (iris4_a1, iris4_a2, iris4_a3)
}

# Margem de erro do sensor
margem_erro = 5

# Função para verificar a autenticidade dos atributos da íris
def autenticar(iris_leitura):
    for usuario, atributos in usuarios.items():
        if all(abs(iris_leitura[i] - atributos[i]) <= margem_erro for i in range(3)):
            return usuario
    return None

# Solicitar ao usuário para inserir a nova leitura do padrão de íris
print("Insira o padrão de íris para autenticação.")
atributo1 = int(input("Atributo 1: "))
atributo2 = int(input("Atributo 2: "))
atributo3 = int(input("Atributo 3: "))

# Coletar os atributos em uma tupla
leitura_iris = (atributo1, atributo2, atributo3)

# Verificar autenticação
usuario_autenticado = autenticar(leitura_iris)

if usuario_autenticado:
    print(f"Autenticação bem-sucedida! \nUsuário: {usuario_autenticado}")
else:
    print("Autenticação falhou!")
