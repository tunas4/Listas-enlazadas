import tkinter as tk
from tkinter import messagebox
from lista_doble1 import ListaDoble

class Views:
    def __init__(self, root):
        self.lista = ListaDoble()
        self.root = root

    def inicializar(self):
        self.lista.inicializar()
        messagebox.showinfo("Éxito", "La lista ha sido vaciada.")

    def mostrar(self):
        window = tk.Toplevel(self.root)
        window.geometry("350x350")
        window.title("Mostrar Lista")

        var = tk.StringVar(value="ascendente")
        tk.Radiobutton(window, text="Ascendente", variable=var, value="ascendente").pack(padx=5, pady=5)
        tk.Radiobutton(window, text="Descendente", variable=var, value="descendente").pack(padx=5, pady=5)

        label_resultado = tk.Label(window, text="", justify=tk.LEFT)
        label_resultado.pack(padx=5, pady=5)

        def mostrar_lista():
            ascendente = var.get() == "ascendente"
            resultado = ""
            if ascendente:
                q = self.lista.p
                while q is not None:
                    resultado += f"{q.datos}\n"
                    q = q.siguiente
            else:
                q = self.lista.f
                while q is not None:
                    resultado += f"{q.datos}\n"
                    q = q.anterior
            label_resultado.config(text=resultado)

        tk.Button(window, text="Mostrar", command=mostrar_lista).pack(padx=5, pady=5)

    def buscar(self):
        window = tk.Toplevel(self.root)
        window.geometry("350x350")
        window.title("Buscar")

        tk.Label(window, text="Valor a buscar:").pack(padx=5, pady=5)
        entry_valor = tk.Entry(window)
        entry_valor.pack(padx=5, pady=5)

        label_resultado = tk.Label(window, text="")
        label_resultado.pack(padx=5, pady=5)

        def buscar_valor():
            valor = entry_valor.get()
            if valor:
                nodo = self.lista.buscarOptimizado(valor)
                if nodo:
                    label_resultado.config(text=f"Elemento encontrado: {nodo.datos}")
                else:
                    label_resultado.config(text="El elemento no está en la lista.")
            else:
                label_resultado.config(text="Por favor ingrese un valor para buscar.")

        tk.Button(window, text="Buscar", command=buscar_valor).pack(padx=5, pady=5)

    def insertar(self):
        window = tk.Toplevel(self.root)
        window.geometry("350x350")
        window.title("Insertar")

        tk.Label(window, text="Valor a insertar:").pack(padx=5, pady=5)
        entry_valor = tk.Entry(window)
        entry_valor.pack(padx=5, pady=5)

        label_resultado = tk.Label(window, text="")
        label_resultado.pack(padx=5, pady=5)

        def insertar_valor():
            valor = entry_valor.get()
            if valor:
                self.lista.insertar_ordenado(valor)
                label_resultado.config(text=f"'{valor}' insertado en la lista.")
            else:
                label_resultado.config(text="Por favor ingrese un valor.")

        tk.Button(window, text="Insertar", command=insertar_valor).pack(padx=5, pady=5)

    def eliminar(self):
        window = tk.Toplevel(self.root)
        window.geometry("350x350")
        window.title("Eliminar")

        tk.Label(window, text="Valor a eliminar:").pack(padx=5, pady=5)
        entry_valor = tk.Entry(window)
        entry_valor.pack(padx=5, pady=5)

        label_resultado = tk.Label(window, text="")
        label_resultado.pack(padx=5, pady=5)

        def eliminar_valor():
            valor = entry_valor.get()
            if valor:
                resultado = self.lista.eliminar(valor)
                label_resultado.config(text=resultado)
            else:
                label_resultado.config(text="Por favor ingrese un valor.")

        tk.Button(window, text="Eliminar", command=eliminar_valor).pack(padx=5, pady=5)

    def modificar(self):
        window = tk.Toplevel(self.root)
        window.geometry("350x350")
        window.title("Modificar")

        tk.Label(window, text="Valor a modificar:").pack(padx=5, pady=5)
        entry_valor = tk.Entry(window)
        entry_valor.pack(padx=5, pady=5)

        tk.Label(window, text="Nuevo valor:").pack(padx=5, pady=5)
        entry_nuevo_valor = tk.Entry(window)
        entry_nuevo_valor.pack(padx=5, pady=5)

        label_resultado = tk.Label(window, text="")
        label_resultado.pack(padx=5, pady=5)

        def modificar_valor():
            valor = entry_valor.get()
            nuevo_valor = entry_nuevo_valor.get()
            if valor and nuevo_valor:
                resultado = self.lista.modificar(valor, nuevo_valor)
                label_resultado.config(text=resultado)
            else:
                label_resultado.config(text="Por favor ingrese ambos valores.")

        tk.Button(window, text="Modificar", command=modificar_valor).pack(padx=5, pady=5)

    def creditos(self):
        window = tk.Toplevel(self.root)
        window.geometry("350x350")
        window.title("Créditos")