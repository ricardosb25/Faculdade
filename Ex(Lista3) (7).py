salario = float(input("Digite seu salario: "))
emp = float(input("Digite o valor do emprestimo: "))
if (salario*0.2 >= emp):
	print("Emprestimo concedio")
else:
    print("Emprestimo não concedido")