produto1 = input("DIGITE O NOME DO PRIMEIRO PRODUTO ")
produto1Preco = float(input(f"DIGITE O PREÇO UNITÁRIO DO(a) {produto1}: "))
produto1Quantidade = int(input(f"DIGITE A QUANTIADADE DO(a) {produto1}: "))

produto2 = input("DIGITE O NOME DO SEGUNDO PRODUTO ")
produto2Preco = float(input(f"DIGITE O PREÇO UNTIÁRIO DO(a) {produto2}: "))
produto2Quantidade = int(input(f"DIGITE A QUANTIADADE DO(a) {produto2}: "))

produto3 = input("DIGITE O NOME DO TERCEIRO PRODUTO ")
produto3Preco = float(input(f"DIGITE O PREÇO UNITÁRIO DO(a) {produto3}: "))
produto3Quantidade = int(input(f"DIGITE A QUANTIADADE DO(a) {produto3}: "))

totalP1 = produto1Preco * produto1Quantidade
totalP2 = produto2Preco * produto2Quantidade
totalP3 = produto3Preco * produto3Quantidade

total = totalP1 + totalP2 + totalP3

print(f"Total: R${total:,.2f}")