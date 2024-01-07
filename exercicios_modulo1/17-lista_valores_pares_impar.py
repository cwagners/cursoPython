import random

listNumeros = list(range(0,999))
random.shuffle(listNumeros)
selectNumeros = []
par = []
impar = []

for i in range(10):
    selectNumeros.append(random.choice(listNumeros))
    
print(selectNumeros)

for j in selectNumeros:
    if j % 2 == 0:
        par.append(j)
           
            
    else:
        impar.append(j)
    selectNumeros.index(j)-1
print(par)
print(impar)            
    