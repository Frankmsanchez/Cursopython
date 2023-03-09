import tkinter as tk

class RadioButtonList:
    def __init__(self, master, options):
        self.options = options
        self.var = tk.StringVar()
        self.var.set(options[0])
        self.buttons = []
        
        for option in options:
            button = tk.Radiobutton(master, text=option, variable=self.var, value=option,
                                    command=self.show_selected_option)
            self.buttons.append(button)
            

        reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.buttons.append(reset_button)
        
        # Mostrar los botones en la ventana
        for button in self.buttons:
            button.pack(anchor=tk.W)

    def show_selected_option(self):
        print("Selected option:", self.var.get())
        
    def reset(self):
        self.var.set(self.options[0])
        self.show_selected_option()

root = tk.Tk()


opciones = ["opcion 1","opcion 2","opcion 3", "opcion 4"]

rb_Lista= RadioButtonList(root,opciones)

root.mainloop()