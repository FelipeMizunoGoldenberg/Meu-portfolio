print("Calculadora de Notas\n")
nota1 = float(input("Primeira Nota: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
formula = (nota1 + nota2 + nota3) / 3
print("Nota Final:", formula)
print(f"Média: {formula: .2f}")
