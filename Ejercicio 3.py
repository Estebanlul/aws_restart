def draw_diamond(characters):
    for i in range(1, characters + 1, 2):
        print(("*" * i).center(characters))

    for i in range(characters - 2, 0, -2):
        print(("*" * i).center(characters))

number = int(input("Ingrese un número de caracteres para el rombo: "))

draw_diamond(number)