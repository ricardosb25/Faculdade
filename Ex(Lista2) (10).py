premio = float(input("Digite o valor do premio:"))
num1 = (premio*1.47) - premio
num2 = (premio*1.34) - premio
num3 = premio - (num1 + num2)
print("Ganhador 1:", num1, "\nGanhador 2:", num2,"\nGanhador 3:", num3)