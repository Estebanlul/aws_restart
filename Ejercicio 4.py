def calculator(option, x, y):
    if option == "Adición":
        return x + y
    elif option == "Sustracción":
        return x - y
    elif option == "Multiplicación":
        return x * y
    elif option == "División":
        return x / y

option = input("Ingrese la operación que desea realizar:\n Adición \n Sustracción \n Multiplicación \n División\n")
if option not in ["Adición", "Sustracción", "Multiplicación", "División"]:
    print("No ha seleccionado una opción válida.")
    exit()

x = float(input("Ingrese el primer valor: "))
y = float(input("Ingrese el segundo valor: "))

result = calculator(option, x, y)
print(result)
