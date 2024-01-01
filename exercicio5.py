def contaLetras(fra):
    countUpper, countLowwer = 0, 0
    for x in fra:        
        if x.isupper():
            countUpper += 1
        elif x.islower():
            countLowwer += 1       
    print(f"total de letras maiusculas: {countUpper} e minusculas: {countLowwer} da frase {len(frase)}")

frase = input("Digite uma frase:\n")
contaLetras(frase)


numeros = [1,4,6,89,77,9, 13, 22, 29, 37, 30]
impar = []
par = []
def parImpar(*args):
    for i in numeros:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
    print(numeros)
    print(impar)
    print(par)
 
parImpar(numeros)               