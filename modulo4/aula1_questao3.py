n1 = int(input("digite valor n1: "))
n2 = int(input("digite valor n2: "))
n3 = int(input("digite valor n3: "))

m = (n1 + n2 + n3)/3

if m>=60: 
    print("Aprovado")
elif m>=40: 
    print("Recuperação")
else: 
    print("Reprovado")
print("Fim")