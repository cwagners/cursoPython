nota1, nota2, nota3, nota4 = 0.0, 0.0, 0.0, 0.0
media = 0.0

nota1 = float(input(f"informe a nota1\n"))
nota2 = float(input(f"informe a nota2\n"))
nota3 = float(input(f"informe a nota3\n"))
nota4 = float(input(f"informe a nota4\n"))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"a media das notas ficou; {media:.2f}")