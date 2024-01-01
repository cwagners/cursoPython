def contaLetras(fra):
    countUpper, countLowwer, i = 0, 0, 0
    while ( i <= len(fra)):
        if fra[i] == " ":
            i += 1
            continue
            
        elif fra[i].isUpper():
            countUpper += 1
            i += 1
        elif fra[i].isLower():
            countLowwer += 1    
            i += 1
    print(f"total de letras maiusculas: {countUpper} e minusculas: {countLowwer}")





frase = input("Digite uma frase:\n")
contaLetras(frase)