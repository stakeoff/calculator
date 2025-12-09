
print("welcome to the calculator")

numero1 = int(input("enter your first number:"))
numero2 = int(input("enter your second number:"))

print("\nwe have 4 kind of count")
print("adition press 1")
print("subtraction press 2")
print("multiplication press 3")
print("division press 4")

adition = 1
subtration = 2
multiplication = 3
division = 4

conta = int(input("choose one:"))

if conta == adition :
    resultado = numero1 + numero2
    print(f"the result is {resultado}")
elif conta == subtration :
    resultado = numero1 - numero2
    print(f"the result is {resultado}")
elif conta == multiplication:
    resultado = numero1 * numero2
    print(f"the result is {resultado}")
else:
    resultado = numero1/numero2
    if numero2 == 0 and conta == 4:
        print("thats number is indivisible.")
    print(f"the result is {resultado}")
