from nodo import Nodo

class Lista:
    p = Nodo()

    def __init__(self):
        self.p = None

    def mostrar_Ite(self):
        if self.p == None:
            print("Lista vacia")
        else:
            q = self.p
            while q != None:
                print(q.datos)
                q = q.siguiente

    def mostrar_Rec(self, n):
        if n == None:
            print("Lista vacia")
        else:
            print(n.datos)
            self.mostrar_Rec(n.siguiente)

    def insertar_inicio(self, v):
        q = Nodo()
        q.datos = v
        q.siguiente = self.p
        self.p = q

    def insertar_final(self, v):
        q = Nodo()
        q.datos = v
        if q == None:
            self.p = q
        else:
            t = self.p
            while t.siguiente != None:
                t = t.siguiente
            t.siguiente = q

    def insertar_antes_de(self, v, x):
        res = Lista.buscar(self, v)
        if res == None:
            return "No se puede insertar"
        else:
            if res.datos == v:
                Lista.insertar_inicio(self, x)
            else:
                q = Nodo()
                q.datos = x
                q.siguiente = res.siguiente
                res.siguiente = q

    def insertar_despues_de(self, v, x):
        res = Lista.buscar(self, v)
        if res == None:
            return "No se puede insertar"
        else:
            if res.datos != v:
                res = res.siguiente
            else:
                q = Nodo()
                q.datos = x
                q.siguiente = res.siguiente
                res.siguiente = q

    def eliminar_inicio(self):
        if self.p == None:
            return self.p
        else:
            q = self.p
            self.p = self.p.siguiente
            q.siguiente = None
            return q

    def eliminar_final(self):
        if self.p == None:
            return self.p
        elif self.p.siguiente == None:
            q = self.p
            self.p = None
        else:
            t = self.p
            q = self.p.siguiente
            while q.siguiente != None:
                t = q
                q = q.siguiente
            t.siguiente = None
        return q

    def eliminar_nodo(self, v):
        res = Lista.buscar(self, v)
        if res == None:
            return "No se puede eliminar"
        else:
            if res.datos == v:
                self.p = self.p.siguiente
                res.siguiente = None
                return res
            else:
                q = res.siguiente
                res.siguiente = q.siguiente
                q.siguiente = None
                return q

    def buscar(self, v):
        if self.p == None:
            return None
        if self.p.siguiente == None:
            if self.p.datos == v:
                return self.p
            else:
                return None
        else:
            if self.p.datos == v:
                return self.p
            else:
                q = self.p
                while q.siguiente != None and q.siguiente.datos != v:
                    q = q.siguiente
                if q.siguiente == None:
                    return None
                else:
                    return q

    def mostrar(self, v):
        res = Lista.buscar(self, v)
        if res == None:
            print("El valor no se encuentra en la lista")
        else:
            print("El valor se encuentra en la lista")

    def modificar_desordenado(self, v, x):
        res = Lista.buscar(self, v)
        if res == None:
            return "Valor no encontrado"
        else:
            if res.datos != v:
                res = res.siguiente
            res.datos = x

    # def modificar_ordenado(self, v, x):

    # def inicializar(self):