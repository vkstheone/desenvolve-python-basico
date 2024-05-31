comprimento = int(input("Digite o Comprimento do Terreno: "))
largura = int(input("Digite a Largura do Terreno: "))
preco_m2 = float(input("Valor do M2: "))

area = comprimento * largura
preco_total = preco_m2*area
print(f"O terreno possui {area} m2 e custa R${preco_total:,.2f}")