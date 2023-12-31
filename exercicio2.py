frase = input("informe uma frase \n")

print( frase[0] + frase[1:].replace(frase[0], "$"))
print(f"frase informada: {frase}\n")

frase1 = input("informe uma frase1 \n")
frase2 = input("informe uma frase2 \n")

print(frase1[0:2])
print(frase1.replace(frase1[0:2], frase2[0:2]) + " " + frase2.replace(frase2[0:2], frase1[0:2]) )