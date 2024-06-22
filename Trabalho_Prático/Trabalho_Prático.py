import csv

# Estruturas de Dados
usuarios = {}
produtos = []

# Funções de Usuários
def carregar_usuarios():
    try:
        with open('usuarios.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                usuarios[row[0]] = {'senha': row[1], 'permissao': row[2]}
    except FileNotFoundError:
        pass

def salvar_usuarios():
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for usuario, detalhes in usuarios.items():
            writer.writerow([usuario, detalhes['senha'], detalhes['permissao']])

def criar_usuario(nome, senha, permissao):
    usuarios[nome] = {'senha': senha, 'permissao': permissao}
    salvar_usuarios()

def listar_usuarios():
    for usuario, detalhes in usuarios.items():
        print(f'Nome: {usuario}, Permissão: {detalhes["permissao"]}')

def atualizar_usuario(nome, nova_senha=None, nova_permissao=None):
    if nome in usuarios:
        if nova_senha:
            usuarios[nome]['senha'] = nova_senha
        if nova_permissao:
            usuarios[nome]['permissao'] = nova_permissao
        salvar_usuarios()
    else:
        print('Usuário não encontrado.')

def deletar_usuario(nome):
    if nome in usuarios:
        del usuarios[nome]
        salvar_usuarios()
    else:
        print('Usuário não encontrado.')

# Funções de Produtos
def carregar_produtos():
    try:
        with open('produtos.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                produtos.append(row)
    except FileNotFoundError:
        pass

def salvar_produtos():
    with open('produtos.csv', mode='w', newline='') as file:
        fieldnames = ['codigo', 'nome', 'preco', 'quantidade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

def criar_produto(codigo, nome, preco, quantidade):
    produtos.append({'codigo': codigo, 'nome': nome, 'preco': preco, 'quantidade': quantidade})
    salvar_produtos()

def listar_produtos():
    for produto in produtos:
        print(f'Código: {produto["codigo"]}, Nome: {produto["nome"]}, Preço: {produto["preco"]}, Quantidade: {produto["quantidade"]}')

def atualizar_produto(codigo, novo_nome=None, novo_preco=None, nova_quantidade=None):
    for produto in produtos:
        if produto['codigo'] == codigo:
            if novo_nome:
                produto['nome'] = novo_nome
            if novo_preco:
                produto['preco'] = novo_preco
            if nova_quantidade:
                produto['quantidade'] = nova_quantidade
            salvar_produtos()
            return
    print('Produto não encontrado.')

def deletar_produto(codigo):
    global produtos
    produtos = [produto for produto in produtos if produto['codigo'] != codigo]
    salvar_produtos()

def buscar_produto(codigo=None, nome=None):
    for produto in produtos:
        if (codigo and produto['codigo'] == codigo) or (nome and produto['nome'] == nome):
            print(f'Código: {produto["codigo"]}, Nome: {produto["nome"]}, Preço: {produto["preco"]}, Quantidade: {produto["quantidade"]}')
            return
    print('Produto não encontrado.')

def ordenar_produtos_por_nome():
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    for produto in produtos_ordenados:
        print(f'Código: {produto["codigo"]}, Nome: {produto["nome"]}, Preço: {produto["preco"]}, Quantidade: {produto["quantidade"]}')

def ordenar_produtos_por_preco():
    produtos_ordenados = sorted(produtos, key=lambda x: x['preco'])
    for produto in produtos_ordenados:
        print(f'Código: {produto["codigo"]}, Nome: {produto["nome"]}, Preço: {produto["preco"]}, Quantidade: {produto["quantidade"]}')

# Carregar dados ao iniciar
carregar_usuarios()
carregar_produtos()

# Menu principal
def menu():
    while True:
        print("\n1. Gerenciar Usuários\n2. Gerenciar Produtos\n3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            gerenciar_usuarios()
        elif escolha == '2':
            gerenciar_produtos()
        elif escolha == '3':
            break
        else:
            print("Opção inválida.")

def gerenciar_usuarios():
    while True:
        print("\n1. Criar Usuário\n2. Listar Usuários\n3. Atualizar Usuário\n4. Deletar Usuário\n5. Voltar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome do usuário: ")
            senha = input("Senha: ")
            permissao = input("Permissão (Admin/Funcionario): ")
            criar_usuario(nome, senha, permissao)
        elif escolha == '2':
            listar_usuarios()
        elif escolha == '3':
            nome = input("Nome do usuário: ")
            nova_senha = input("Nova senha (deixe em branco para não alterar): ")
            nova_permissao = input("Nova permissão (deixe em branco para não alterar): ")
            atualizar_usuario(nome, nova_senha, nova_permissao)
        elif escolha == '4':
            nome = input("Nome do usuário: ")
            deletar_usuario(nome)
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")

def gerenciar_produtos():
    while True:
        print("\n1. Criar Produto\n2. Listar Produtos\n3. Atualizar Produto\n4. Deletar Produto\n5. Buscar Produto\n6. Ordenar por Nome\n7. Ordenar por Preço\n8. Voltar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            codigo = input("Código do produto: ")
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            criar_produto(codigo, nome, preco, quantidade)
        elif escolha == '2':
            listar_produtos()
        elif escolha == '3':
            codigo = input("Código do produto: ")
            novo_nome = input("Novo nome (deixe em branco para não alterar): ")
            novo_preco = input("Novo preço (deixe em branco para não alterar): ")
            nova_quantidade = input("Nova quantidade (deixe em branco para não alterar): ")
            atualizar_produto(codigo, novo_nome, float(novo_preco) if novo_preco else None, int(nova_quantidade) if nova_quantidade else None)
        elif escolha == '4':
            codigo = input("Código do produto: ")
            deletar_produto(codigo)
        elif escolha == '5':
            codigo = input("Código do produto (deixe em branco para buscar por nome): ")
            nome = input("Nome do produto (deixe em branco para buscar por código): ")
            buscar_produto(codigo if codigo else None, nome if nome else None)
        elif escolha == '6':
            ordenar_produtos_por_nome()
        elif escolha == '7':
            ordenar_produtos_por_preco()
        elif escolha == '8':
            break
        else:
            print("Opção inválida.")

menu()
