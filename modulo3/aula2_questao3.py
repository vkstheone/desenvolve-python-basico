idade = int(input("Digite Sua Idade: "))
jaJogou = bool(input("Ja Jogou Pelo menos 3 jogos de Tabuleiro?:"))
jogosVencidos = int(input("Quantos Jogos Ja venceu?:"))

apto = (idade >= 16 and idade <= 18 )and (jaJogou == True)  and (jogosVencidos >=1)

print(apto)