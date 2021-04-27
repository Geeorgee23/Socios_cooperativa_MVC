class Socios:

    def __init__(self,id_socio,dni,nombre,apellidos,fecha):
        self.id_socio=id_socio
        self.dni=dni
        self.nombre=nombre
        self.apellidos=apellidos
        self.fecha=fecha
        self.saldo=0.0
        self.registrosPendientes={}


    def getIdSocio(self):
        return self.id_socio
    
    def getDni(self):
        return self.dni
    
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getFecha(self):
        return self.fecha

    def getSaldo(self):
        return self.saldo

    def getRegistrosPendientes(self):
        return self.registrosPendientes

    def addProducto(self,producto,kilos):
        if producto in self.registrosPendientes:
            self.registrosPendientes[producto] += kilos
        else:
            self.registrosPendientes[producto] = kilos


    def actualizaSaldo(self,saldo):
        self.saldo+=saldo


    def delRegistros(self):
        self.registrosPendientes={}
    

