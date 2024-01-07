num1 = int(input("Informe o primeiro número inteiro\n"))
num2 = int(input("Informe o segundo número inteiro\n"))
num3 = float(input("Informe o número real(float)\n"))

def potencia(base, expoente):
          resultado = base ** expoente
          return resultado
 
result = potencia(num3, 3)    
produto = (num1 * 2) + (num2/2)
produto2 = (num1 * 3) + (num3)

print(f"o produto do dobro do primeiro com metade do segundo: {produto}\n")
print(f"a soma do triplo do primeiro com o terceiro: {produto2}\n")
print(f"o terceiro elevado ao cubo: {result}\n")