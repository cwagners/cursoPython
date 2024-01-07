maxNotas = 4
notas = []
media = 0.0
while(maxNotas!= 0):
    nota = float(input(f"Informe a nota: {maxNotas}\n"))
    notas.append(nota)
    media = media + nota
    maxNotas -= 1
    print(notas)
media = media / (len(notas))
print(f"A Lista informada: {notas}\n\n")
print(f"A media das notas é: {media:.2f}")   