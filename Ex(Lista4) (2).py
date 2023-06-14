ListaA = []
for n in range(0,15):
    num = int(input("Insira um número: "))
    ListaA.append(num)
x = int(input("Insira o valor x: "))
ListaB = []
for n in ListaA:
    if n > x:
        ListaB.append(n)
print(ListaB)