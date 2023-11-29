import tkinter as tk

def mostrar_mensaje():
    label.config(text="Hola, Tkinter!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Semi-Científica")

# Crear un botón
boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack(pady=10)

# Crear una etiqueta
label = tk.Label(ventana, text="¡Bienvenido a Tkinter!")
label.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()