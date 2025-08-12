# Aprovação de aluno
# Faça um programa que leia três notas, calcule e mostre a média aritmética entre elas, se a média aritmética for:
    # Média maior ou igual a 7 – ALUNO APROVADO
    # Média maior ou igual a 5 e menor que 7 – ALUNO EM RECUPERAÇÃO
    # Média menor que 5 – ALUNO REPROVADO

grade1 = float(input("Enter your first grade: "))
grade2 = float(input("Enter your second grade: "))
grade3 = float(input("Enter your third grade: "))
grade4 = float(input("Enter your fourth grade: "))

average = (grade1 + grade2 + grade3 + grade4) / 4

if average >= 6:
    print(f"Congratulations! You passed, your final grade was {average:.1f}.")
elif 5 <= average < 6:
    print(f"You have to take recovery exams, your final grade was {average:.1f}.")
else:
    print(f"You failed, your final grade was {average:.1f}.")
