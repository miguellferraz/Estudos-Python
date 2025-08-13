# Classificação etária
# Peça a idade de uma pessoa e classifique-a como "Adulto", "Juvenil", "Infantil" ou "Mirim"

def ageFunction():
    age = int(input("\nEnter your age: "))

    if age < 4:
        print("You are a baby")
    elif age >= 4 and age < 14:
        print("You are a child")
    elif age >= 14 and age < 18:
        print("You are young")
    elif age >= 18 and age < 50:
        print("You are an adult")
    elif age >= 50:
        print("You are an elderly person")
    elif age < 0:
        print("You haven't even been born yet.")

while True:
    choice = input("\nDo you want to run the program? (y/n): ").lower()
    
    if choice == "n":
        print("\nProgram closed.")
        break
    elif choice == "y":
        print("\nRunning the program...")
        ageFunction()

    else:
        print("Invalid option, enter 'y' or 'n'.")