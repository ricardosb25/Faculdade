lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print('A :', lista[1:10])
print('B :', lista[9:14])
print('C :', lista[2:16:2])
print('D :', lista[1:16:2])
print('E :', lista[2:16:2], lista[3:16:3], lista[4:16:4])
reverso = lista[:]
reverso.reverse()
print('F :', reverso)
x = sum(lista[10:16])
print('G :', x)
novo = lista[:]
novo.append(16)
print('H :', novo)
troca = lista[:]
troca.insert(6, 17)
troca.remove(6)
print('I :', troca)
