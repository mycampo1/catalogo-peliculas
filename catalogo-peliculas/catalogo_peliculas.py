import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    
    root.title('Catalogo de peliculas')
    root.iconbitmap('img/bitcoin.ico')
    root.resizable(0,0) # type: ignore
    
    #Esto funciona sin empaquetar el frame
    # frame = tk.Frame(root, width=480, height=320) se puede usar asi tambien.
    #frame = tk.Frame(root)
    #frame.pack()
    #frame.config(width=480, height=320)
    
    app = Frame(root = root)
    
    barra_menu(root)
    
    app.mainloop()
    
    

if __name__ == '__main__':
    main() 