num1 = float(input("Digite um numero: "))
if(num1 %2 == 0 and num1 %3 == 0):
	print("Divisivel por 2 e 3")
elif(num1 %5 ==0):
	print("Divisivel por 5")
elif(num1 %7 == 0):
	print("Divisivel por 7")
else:
	print("Erro")