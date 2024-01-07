import random
import string

letras = string.ascii_uppercase
listLetters = []
tuplaVogais = ('A', 'E','I', 'O', 'U')
listConsoantes = []
consoantes = 0
for i in range (10):
    listLetters.append(random.choice(letras))

for j in listLetters:
    if j not in tuplaVogais:
        consoantes += 1
        listConsoantes.append(j)
print(listLetters)
print(consoantes) 
print(listConsoantes)     