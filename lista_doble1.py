from nodo import Nodo

class ListaDoble:
    def __init__(self):
        self.p = None
        self.f = None

    def insertar_ordenado(self, v):
        nuevo = Nodo()
        nuevo.datos = v

        if self.p is None:
            self.p = nuevo
            self.f = nuevo
            return

        desde_final = ord(v[0].lower()) >= ord('m')

        if desde_final:
            actual = self.f
            while actual is not None:
                if v.lower() > actual.datos.lower():
                    self._insertar_despues(actual, nuevo)
                    return
                elif v.lower() <= actual.datos.lower() and actual.anterior is None:
                    self._insertar_antes(actual, nuevo)
                    return
                actual = actual.anterior
        else:
            actual = self.p
            while actual is not None:
                if v.lower() < actual.datos.lower():
                    self._insertar_antes(actual, nuevo)
                    return
                elif v.lower() >= actual.datos.lower() and actual.siguiente is None:
                    self._insertar_despues(actual, nuevo)
                    return
                actual = actual.siguiente

    def _insertar_antes(self, actual, nuevo):
        nuevo.siguiente = actual
        nuevo.anterior = actual.anterior
        if actual.anterior is not None:
            actual.anterior.siguiente = nuevo
        actual.anterior = nuevo
        if actual == self.p:
            self.p = nuevo

    def _insertar_despues(self, actual, nuevo):
        nuevo.anterior = actual
        nuevo.siguiente = actual.siguiente
        if actual.siguiente is not None:
            actual.siguiente.anterior = nuevo
        actual.siguiente = nuevo
        if actual == self.f:
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

    def buscarOptimizado(self, v):
        if self.p is None:
            return None

        ascii_valor = ord(v[0].lower())
        q = None

        if ascii_valor < ord('m'):
            q = self.p
            while q is not None:
                if q.datos.lower() == v.lower():
                    return q
                elif q.datos.lower() > v.lower():
                    break
                q = q.siguiente
        else:
            q = self.f
            while q is not None:
                if q.datos.lower() == v.lower():
                    return q
                elif q.datos.lower() < v.lower():
                    break
                q = q.anterior

        return None

    def eliminar(self, v):
        if self.p is None:
            return "La lista está vacía, no se puede eliminar ningún elemento."

        nodo_encontrado = self.buscarOptimizado(v)

        if nodo_encontrado is None:
            return "No se encontró la cadena en la lista."

        if self.p == self.f:
            self.p = None
            self.f = None
            return f"Se eliminó '{v}'. La lista quedó vacía."

        if nodo_encontrado == self.p:
            self.p = nodo_encontrado.siguiente
            self.p.anterior = None
            nodo_encontrado.siguiente = None
            return f"Se eliminó '{v}' del inicio de la lista."

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

    def modificar(self, valor, nuevo_valor):
        if self.p is None:
            return "La lista está vacía, no se puede modificar ningún elemento."
    
        nodo = self.buscarOptimizado(valor)
        if nodo is None:
            return "No se encuentra el valor en la lista."
    
        resultado_eliminar = self.eliminar(valor)
        if "Se eliminó" not in resultado_eliminar:
            return "Error al intentar modificar el elemento."

        self.insertar_ordenado(nuevo_valor)
        return f"Se modificó '{valor}' por '{nuevo_valor}' exitosamente."