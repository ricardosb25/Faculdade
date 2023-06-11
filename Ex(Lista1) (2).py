idade = float(input("Digite sua idade:"))
mes = float(input("Quantos meses desde o ultimo aniversario:"))
dia = float(input("Quantos dias desde o ultimo aniversario:"))
anos = idade * 365 + mes *30 + dia
print("Você está vivo a:", "%.2f" % anos, "dias")