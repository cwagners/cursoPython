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