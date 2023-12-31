kmPercorrido = int(input("Informe em KM a distancia a ser percorrida:\n"))
valorTotal = 0.00
if kmPercorrido <= 200:
    valorTotal = kmPercorrido * 0.50
    print(valorTotal)
else:
    valorTotal = kmPercorrido * 0.35
    print(valorTotal) 
    
salario = float(input("Informe o salario:\n"))    
aumento = 0.00
if salario > 1250.00:
    aumento = salario * 0.10
    print(aumento)
elif salario <=1250.00:
    aumento = salario * 0.15
    print(aumento)
    