import tkinter as tk
from views import Views

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ListaDoblementeEnlazada")
        self.views = Views(self.root)
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        btn_inicializar = tk.Button(frame, text="Inicializar / Borrar lista", command=self.views.inicializar)
        btn_inicializar.pack(padx=5, pady=5)

        btn_mostrar = tk.Button(frame, text="Mostrar lista", command=self.views.mostrar)
        btn_mostrar.pack(padx=5, pady=5)

        btn_buscar = tk.Button(frame, text="Buscar", command=self.views.buscar)
        btn_buscar.pack(padx=5, pady=5)

        btn_insertar = tk.Button(frame, text="Insertar", command=self.views.insertar)
        btn_insertar.pack(padx=5, pady=5)

        btn_eliminar = tk.Button(frame, text="Eliminar", command=self.views.eliminar)
        btn_eliminar.pack(padx=5, pady=5)

        btn_modificar = tk.Button(frame, text="Modificar", command=self.views.modificar)
        btn_modificar.pack(padx=5, pady=5)

        btn_creditos = tk.Button(frame, text="Creditos", command=self.views.creditos)
        btn_creditos.pack(padx=5, pady=5)

        btn_salir = tk.Button(frame, text="Salir", command=self.root.destroy)
        btn_salir.pack(padx=5, pady=5)

if __name__ == "__main__":
    Main()