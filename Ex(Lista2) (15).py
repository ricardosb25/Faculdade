salarioBase = float(input("Digite o salario base:"))
bonus = salarioBase *1.05
imposto = salarioBase * 0.07
total = bonus - imposto
print("O salario é de:",  total)