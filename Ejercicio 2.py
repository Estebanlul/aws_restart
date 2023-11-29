def counting(phrase):
    counting_characters = len(phrase)
    return counting_characters

input_phrase = input("Ingrese una frase: ")

result = counting(input_phrase)
print(f"La frase tiene {result} caracteres.")