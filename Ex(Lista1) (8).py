veloI = float(input("Insira a velocidade incial em m/s:"))
veloF = float(input("Insira a velocidade final em m/s:"))
deltaT = float(input("Insira a variação de tempo em segundos:"))
aceleracao = (veloF - veloI)/ deltaT
print("A aceleração é de:", aceleracao, "m/s²")