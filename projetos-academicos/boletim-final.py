print("Boletim Final:\n")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("Média Aritmética =", media)

if media < 6:
    print("Aluno Reprovado.")
elif media >= 9:
    print("ALUNO APROVADO!")
else:
    print("Aluno Aprovado.")
