import tkinter as tk
from tkinter import messagebox
from lista_doble import ListaDoble

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("ListaDoblementeEnlazada")
        self.lista = ListaDoble()

        tk.Label(root, text="Valor:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_valor = tk.Entry(root)
        self.entry_valor.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(root, text="Insertar al Inicio", command=self.insertar_inicio).grid(row=1, column=0, pady=5)
        tk.Button(root, text="Insertar al Final", command=self.insertar_final).grid(row=1, column=1, pady=5)
        tk.Button(root, text="Mostrar Lista", command=self.mostrar_lista).grid(row=2, column=0, pady=5)
        tk.Button(root, text="Buscar", command=self.buscar).grid(row=2, column=1, pady=5)
        tk.Button(root, text="Insertar Antes De", command=self.insertar_antes_de).grid(row=3, column=0, pady=5)
        tk.Button(root, text="Inicializar Lista", command=self.inicializar).grid(row=3, column=1, pady=5)

        self.resultado = tk.Text(root, width=50, height=10, state='disabled')
        self.resultado.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def insertar_inicio(self):
        valor = self.entry_valor.get()
        if valor:
            self.lista.insertar_inicio(valor)
            messagebox.showinfo("Éxito", f"'{valor}' insertado al inicio de la lista.")
        else:
            messagebox.showwarning("Error", "Por favor ingrese un valor.")

    def insertar_final(self):
        valor = self.entry_valor.get()
        if valor:
            self.lista.insertar_final(valor)
            messagebox.showinfo("Éxito", f"'{valor}' insertado al final de la lista.")
        else:
            messagebox.showwarning("Error", "Por favor ingrese un valor.")

    def mostrar_lista(self):
        self.resultado.config(state='normal')
        self.resultado.delete(1.0, tk.END)
        ascendente = messagebox.askyesno("Mostrar Lista", "¿Mostrar ascendentemente?")
        if ascendente:
            q = self.lista.p
            while q is not None:
                self.resultado.insert(tk.END, f"{q.datos}\n")
                q = q.siguiente
        else:
            q = self.lista.f
            while q is not None:
                self.resultado.insert(tk.END, f"{q.datos}\n")
                q = q.anterior
        self.resultado.config(state='disabled')

    def buscar(self):
        valor = self.entry_valor.get()
        if valor:
            nodo = self.lista.buscar(valor)
            if nodo:
                messagebox.showinfo("Resultado", f"Elemento encontrado: {nodo.datos}")
            else:
                messagebox.showwarning("No encontrado", "El elemento no está en la lista.")
        else:
            messagebox.showwarning("Error", "Por favor ingrese un valor para buscar.")

    def insertar_antes_de(self):
        valor = self.entry_valor.get()
        if valor:
            resultado = self.lista.insertar_antes_de(valor)
            if resultado == "No se puede insertar":
                messagebox.showwarning("Error", f"'{valor}' no se encontró en la lista.")
            else:
                messagebox.showinfo("Éxito", "Elemento insertado antes de '{valor}'.")
        else:
            messagebox.showwarning("Error", "Por favor ingrese un valor.")

    def inicializar(self):
        self.lista.inicializar()
        messagebox.showinfo("Éxito", "La lista ha sido vaciada.")
        self.resultado.config(state='normal')
        self.resultado.delete(1.0, tk.END)
        self.resultado.config(state='disabled')




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()