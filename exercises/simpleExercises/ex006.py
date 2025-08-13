# Tabuada
# Peça um número inteiro e exiba a tabuada desse número de 1 a 10

def tableFunction():
    number = int(input("Enter a number: "))

    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

while True:
    choice = str(input("\nDo you want to run the program? (y/n): "))

    if choice == "n":
        print("Program closed.")
        break
    elif choice == "y":
        print("Running the program...")
        tableFunction()
    else:
        print("Invalid option, enter 'y' or 'n'.")
