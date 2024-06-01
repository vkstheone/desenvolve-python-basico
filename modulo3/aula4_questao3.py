ano = int(input("Digite o ano: "))
bissexto = ""

if(ano % 4 == 0 and ano % 100 > 0):
    bissexto = "bissexto"
    if(ano % 400 == 0):
        bissexto = "bissexto2"
else: bissexto = "Não bissexto"

print(bissexto)