peso = float(input("Digite seu peso:"))
gordo = (peso *0.15) + peso
magro = peso - (peso *0.2)
print("Se engordar 15% é de","%.2f" % gordo, "\nSe emagrecer 20% é de","%.2f" % magro)