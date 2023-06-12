salario = float(input("Digite o salario:"))
conta1 = float(input("Digite o valor da primeira conta:"))
conta2 = float(input("Digite o valor da segunda conta:"))
NC1 = conta1 * 1.02
NC2 = conta2 * 1.02
total = salario - (NC2 + NC1)
print("O resto do salario é de:", total)