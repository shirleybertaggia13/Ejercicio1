class Email:
    __idCuenta = 0
    __dominio = 0
    __tipoDominio = 0
    __contraseña = 0
    def __init__(self, idCuenta, dominio, tipoDominio, contraseña=""):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contraseña = contraseña
    def getDominio(self):
        return self.__dominio
    def setContraseña(self, v):
        self.__contraseña = v
    def getContraseña(self):
        return self.__contraseña
    def retornaEmail(self):
        return self.__idCuenta+"@"+self.__dominio+"."+self.__tipoDominio
    def verificaContraseña(self, contraseña):
        return self.__contraseña==contraseña