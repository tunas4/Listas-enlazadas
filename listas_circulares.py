from nodo import Nodo

class lista_circular:
    def __init__(self):
        self.p = None

    def mostrar_Ite(self):
        if self.p == None:
            print("Lista vacia")
        else:
            q = self.p
            while q != self.p:
                print(q.datos)
                q = q.siguiente

    def insertar_inicio(self, v):
        q = Nodo()
        q.datos = v
        if self.p == None:
            q.siguiente = q
        else:
            t = self.p
            while t.siguiente != self.p:
                t = t.siguiente
            q.siguiente = self.p
            t.siguiente = q
        self.p = q

    def insertar_final(self, v):
        q = Nodo()
        q.datos = v
        if self.p == None:
            q.siguiente = q
        else:
            t = self.p
            while t.siguiente != self.p:
                t = t.siguiente
            t.siguiente = q
            q.siguiente = self.p
        q.siguiente = self.p

    def eliminar_inicio(self):
        if self.p == None:
            return None
        
        q = self.p
        if self.p.siguiente == self.p:
            self.p = None
            q.siguiente = None
        else:
            t = self.p
            while t.siguiente != self.p:
                t = t.siguiente
            self.p = q.siguiente
            q.siguiente = None
            t.siguiente = self.p
        return q
    
    def eliminar_final(self):
        if self.p == None:
            return None
        
        q = self.p
        if self.p.siguiente == self.p:
            self.p = None
            q.siguiente = None
        else:
            t = self.p
            q = q.siguiente
            while q.siguiente != self.p:
                t = q
                q = q.siguiente
            q.siguiente = None
            t.siguiente = self.p
        return q
    
    def buscar(self, v):
        if self.p == None:
            return None
        
        if self.p.siguiente == self.p:
            if self.p.datos == v:
                return self.p
            else:
                return None
        else:
            if self.p.datos == v:
                return self.p
            else:
                q = self.p
                while (q.siguiente).datos != v and q.siguiente != self.p:
                    q = q.siguiente
                if q.siguiente == None:
                    return None
                else:
                    return q

    def eliminar_nodo(self, v):
        res = lista_circular.buscar(self, v)
        if res == None:
            return "No se puede eliminar"
        else:
            if res.datos == v:
                t = lista_circular.eliminar_inicio(self)
                return t
            else:
                q = res.siguiente
                res.siguiente = q.siguiente
                q.siguiente = None
                return q

    