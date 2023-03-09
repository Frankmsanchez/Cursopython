import tkinter as tk

ventana = tk.Tk()

label = tk.Label(ventana, text="Selecciona un elemento:")

opciones = ["Opción 1", "Opción 2", "Opción 3","Opcion 4"]
var_opcion = tk.StringVar(value=opciones[0]) 
lista_opciones = tk.OptionMenu(ventana, var_opcion, *opciones)


label.pack()
lista_opciones.pack()

ventana.mainloop()