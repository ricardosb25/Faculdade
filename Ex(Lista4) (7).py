idade = int(input("Digite sua idade: "))
if idade <0:
	print ("Você ainda vai nascer:")
elif idade <= 3:
	print("Você ainda é um bebê")
elif idade < 13:
	print("Você é um criança")
elif idade < 18:
	print("Você é um adolescente")
elif idade < 60:
	print("Você é um adulto")
elif idade < 100:
	print("Você é um idoso")
elif idade >= 100:
	print("Volte para o museu")
else:
	print("Erro")