import tkinter as tk


#creacion de barra de menu
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)
    
    menu_inico = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inico)
    
    menu_inico.add_command(label='Crear registro en DB')
    menu_inico.add_command(label='Eliminar registro en DB')
    menu_inico.add_command(label='Salir', command=root.destroy)
    
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Confirguracion')
    barra_menu.add_cascade(label='Ayuda')

#creacion del frame
class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.config(width=480, height=320)
        
        self.campos_pelicula()
        
    def campos_pelicula(self):
        #Label de cada campo
        self.label_nombre = tk.Label(self, text='Nombre:')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_duracion = tk.Label(self, text='Duración:')
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_genero = tk.Label(self, text='Genero:')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)
        
    