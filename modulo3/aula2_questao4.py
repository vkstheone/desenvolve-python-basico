classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

guerreiro = (classe == 'guerreiro' and forca >=15) and (magia <=10)
mago = (classe == 'mago' and forca <=10) and (magia >=15)
arqueiro = (classe == 'arqueiro' and forca >=5 and forca<=15) and (magia >= 5 and magia <=15)

compativel = guerreiro or mago or arqueiro

print(compativel)