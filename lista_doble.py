from nodo import Nodo

class ListaDoble:
    def __init__(self):
        self.p = None
        self.f = None

    def mostrar(self):
        if self.p is None: #Lista vacia
            print("Lista vacia")
        else:
            if self.p == self.f: #Lista con un solo elemento
                print(self.p.datos)
            else:
                print("¿Mostrar Ascendentemente? (si/no)")
                resp = input().lower()

                if resp == "si": #Mostrar Ascendentemente
                    q = self.p
                    while q is not None:
                        print(q.datos)
                        q = q.siguiente
                elif resp == "no": #Mostrar Descendentemente
                    q = self.f
                    while q is not None:
                        print(q.datos)
                        q = q.anterior
                else:
                    print("Respuesta no reconocida")
    
    def insertar_inicio(self, v):
        q = Nodo()
        q.datos = v
        q.siguiente = self.p
        if self.p is None:
            self.f = q
        else:
            self.p.anterior = q
        self.p = q
    
    def buscarOptimizado(self, v):
        
        if self.p is None:
            return None
        
        ascii_valor = ord(v[0].lower())
        q = None

        if ascii_valor < ord('m'):
            q = self.p # Comienza desde el inicio
            while q is not None: # Mientras no sea el final
                if q.datos.lower() == v.lower():
                    print("Palabra Encontrada")
                    return q
                elif q.datos.lower() > v.lower():
                    break
                q = q.siguiente # Avanzamos al siguiente nodo
        else:
            q = self.f # Comienza desde el final
            while q is not None: # Mientras no sea el final
                if q.datos.lower() == v.lower():
                    print("Palabra Encontrada")
                    return q
                elif q.datos.lower() < v.lower():
                    break
                q = q.anterior # Avanzamos al siguiente nodo

        print("Palabra no encontrada")
        return None
            
    def insertar_ordenado(self, v):
    # Validación de entrada
        if not v or not isinstance(v, str):
            print("Entrada inválida. Debe ser una cadena no vacía.")
            return

        nuevo = Nodo()
        nuevo.datos = v

        # Caso 1: Lista vacía
        if self.p is None:
            self.p = nuevo
            self.f = nuevo
            return

        # Decidir dirección de búsqueda basado en la primera letra
        desde_final = ord(v[0].lower()) >= ord('m')  # Desde final si >= 'm'

        # Búsqueda e inserción
        if desde_final:
            # Búsqueda desde el final
            actual = self.f
            while actual is not None:
                if v.lower() > actual.datos.lower():  # Insertar después
                    self._insertar_despues(actual, nuevo)
                    return
                elif v.lower() <= actual.datos.lower() and actual.anterior is None:  # Insertar al inicio
                    self._insertar_antes(actual, nuevo)
                    return
                actual = actual.anterior
        else:
            # Búsqueda desde el inicio
            actual = self.p
            while actual is not None:
                if v.lower() < actual.datos.lower():  # Insertar antes
                    self._insertar_antes(actual, nuevo)
                    return
                elif v.lower() >= actual.datos.lower() and actual.siguiente is None:  # Insertar al final
                    self._insertar_despues(actual, nuevo)
                    return
                actual = actual.siguiente

    # Métodos auxiliares para insertar antes o después de un nodo
    def _insertar_antes(self, actual, nuevo):
        nuevo.siguiente = actual
        nuevo.anterior = actual.anterior
        if actual.anterior is not None:
            actual.anterior.siguiente = nuevo
        actual.anterior = nuevo
        if actual == self.p:  # Actualizar el inicio
            self.p = nuevo

    def _insertar_despues(self, actual, nuevo):
        nuevo.anterior = actual
        nuevo.siguiente = actual.siguiente
        if actual.siguiente is not None:
            actual.siguiente.anterior = nuevo
        actual.siguiente = nuevo
        if actual == self.f:  # Actualizar el final
            self.f = nuevo

    def inicializar(self):
        if self.p is None:
            return "La lista ya está vacía."
        
        q = self.p
        while q is not None:
            temp = q.siguiente
            q.siguiente = None
            q.anterior = None
            q = temp
        
        self.p = None
        self.f = None
        
        return "Lista vaciada por completo."

    def eliminar(self, v):
        if self.p is None:
            return "La lista está vacía, no se puede eliminar ningún elemento."

        # Utilizamos el método buscar que ya teníamos
        nodo_encontrado = self.buscarOptimizado(v)

        # Si no se encontró el valor
        if nodo_encontrado is None:
            return "No se encontró la cadena en la lista."

        # Caso 1: Es el único nodo en la lista
        if self.p == self.f:
            self.p = None
            self.f = None
            return f"Se eliminó '{v}'. La lista quedó vacía."

        # Caso 2: Es el primer nodo
        if nodo_encontrado == self.p:
            self.p = nodo_encontrado.siguiente
            self.p.anterior = None
            nodo_encontrado.siguiente = None
            return f"Se eliminó '{v}' del inicio de la lista."

        # Caso 3: Es el último nodo
        if nodo_encontrado == self.f:
            self.f = nodo_encontrado.anterior
            self.f.siguiente = None
            nodo_encontrado.anterior = None
            return f"Se eliminó '{v}' del final de la lista."
        
        nodo_encontrado.anterior.siguiente = nodo_encontrado.siguiente
        nodo_encontrado.siguiente.anterior = nodo_encontrado.anterior
        nodo_encontrado.siguiente = None
        nodo_encontrado.anterior = None
        return f"Se eliminó '{v}' de la lista."
        

    def modificar(self, v):
        if self.p is None:
            return "La lista está vacía, no se puede modificar ningún elemento."
    
        # Verificamos si el valor existe usando buscar
        nodo = self.buscarOptimizado(v)
        if nodo is None:
            return "No se encuentra el valor en la lista."
    
        print("Ingrese el nuevo valor:")
        nuevo_valor = input()
    
        # Eliminamos el nodo original
        resultado_eliminar = self.eliminar(v)
        if "Se eliminó" not in resultado_eliminar:
            return "Error al intentar modificar el elemento."
    
        # Insertamos el nuevo valor de forma ordenada
        self.insertar_ordenado(nuevo_valor)
    
        return f"Se modificó '{v}' por '{nuevo_valor}' exitosamente."

lista = ListaDoble()

lista.insertar_ordenado("arbol")
lista.insertar_ordenado("casa")
lista.insertar_ordenado("zebra")
lista.insertar_ordenado("gato")
lista.insertar_ordenado("perro")
lista.mostrar()

lista.buscarOptimizado("perro")

lista.modificar("perro")

lista.mostrar()

lista.eliminar("gato")
lista.eliminar("nana")

lista.inicializar()
lista.mostrar()



