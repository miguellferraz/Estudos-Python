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
