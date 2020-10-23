from email import Email
from manejador import manejador

if __name__=='__main__':
    print("Ingrese nombre")
    nombre=input()
    print("Ingrese su id de cuenta")
    idCuenta=input()
    print("Ingrese su dominio")
    dominio=input()
    print("Ingrese su tipo de dominio")
    tipoDominio=input()
    print("Ingrese su contraseña")
    contraseña=input()
    mail=Email(idCuenta,dominio,tipoDominio,contraseña)
    print("Estimado",nombre,"te enviaremos tus mensajes a la direccion",idCuenta+"@"+dominio+"."+tipoDominio)
    print("Ingrese su contraseña actual")
    contraseña=input()
    if(mail.verificaContraseña(contraseña)):
        print("Ingrese su nueva contraseña")
        mail.setContraseña(input())
    else:
        print("Contraseña incorrecta")
    print(mail.getContraseña())
    me = manejador()
    me.testEmail()
    dom=input("Ingrese un dominio:")
    cant=me.buscarEmailsPorDominio(dom)
    print("Cantidad de emails con ese dominio:",cant)
