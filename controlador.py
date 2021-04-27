from socios import Socios


class Controlador:

    def __init__(self):
        self.listaSocios={}
        self.productos = { 'Naranja':40,
                           'Oliva':10,
                           'Caqui':20 }


    def numSocios(self):
        return len(self.listaSocios)

    
    def addSocio(self,socio):
        if (socio.getIdSocio() not in self.listaSocios):
            self.listaSocios[socio.getIdSocio()]=socio
            return True

        return False


    def delSocio(self,id_socio):
        if id_socio in self.listaSocios:
            del self.listaSocios[id_socio]
            return True

        return False


    def listarSocios(self):
        lista=[]
        for clave,valor in self.listaSocios.items():
            lista.append("Id_socio: "+clave+"\n\tDni: "+valor.getDni()+"\n\tNombre: "+valor.getNombre()+"\n\tApellidos: "+valor.getApellidos()+"\n\tfecha: "+valor.getFecha()+"\n\tSaldo: "+str(valor.getSaldo()))

        return lista


    def getProductos(self):
        lista=""
        for i in self.productos:
            lista +="\t"+i+"\n"
           
        return lista




    def addProducto(self,id_socio,producto,kilos):
        if id_socio in self.listaSocios:
            if producto in self.productos:
                self.listaSocios[id_socio].addProducto(producto,kilos)
                return True
        return False




    def actualizaSaldo(self,id_socio):
        saldo=0.0
        if id_socio in self.listaSocios:
            for clave,valor in self.listaSocios[id_socio].getRegistrosPendientes().items():
                saldo+= self.productos[clave] * float(valor)

            self.listaSocios[id_socio].actualizaSaldo(saldo)
            self.listaSocios[id_socio].delRegistros()
            return True

        return False


    def fichaSocio(self,id_socio):
        socio=""
        if id_socio in self.listaSocios:
            for clave,valor in self.listaSocios.items():
                socio = ("Id_socio: "+clave+"\n\tDni: "+valor.getDni()+"\n\tNombre: "+valor.getNombre()+"\n\tApellidos: "+valor.getApellidos()+"\n\tfecha: "+valor.getFecha()+"\n\tSaldo: "+str( "{:10.2f}".format(valor.getSaldo()))+"\n\tRegistros Pendientes: "+str(valor.getRegistrosPendientes()))

        return socio




