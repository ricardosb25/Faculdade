kg = float(input("Digite o peso em kilogramas:"))
cat = int(input("Digite o numero de gatos:"))
peso = kg*1000
catFood = peso/ cat
total = catFood / 5
print("A quantidade para cada gato durante 5 dias é de:","%.2f" % total)