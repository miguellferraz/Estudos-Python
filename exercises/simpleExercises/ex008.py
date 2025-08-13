# Soma de números pares
# Solicite números ao usuário até que ele digite 0. Some apenas os números paresdigitados.
pairs = 0

while True:
    number = int(input("Enter a number: "))
    
    if number == 0:
        print(f"\nThe sum of the pairs is: {pairs}")
        break
    if number % 2 == 0:
        pairs += number
