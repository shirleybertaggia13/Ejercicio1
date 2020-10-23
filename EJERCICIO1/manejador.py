import csv
from email import Email

class manejador:
    def __init__(self):
        self.__listaEmails = []
    def agregarEmail(self,unEmail):
        self.__listaEmails.append(unEmail)
    def buscarEmailsPorDominio(self, dominio):
        i=0
        for email in self.__listaEmails:
            if email.getDominio() == dominio:
                i=i+1
        return i
    def getEmail(self, numero):
        return self.__listaEmails[numero]
    def __str__(self):
        s = ""
        for email in self.__listaEmails:
            s+= str(email) + '\n'
        return s
    def testEmail(self):
        archivo = open('Emails.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            lista=fila[0].split('@')
            unEmail = Email(lista[0], lista[1], lista[2])
            self.agregarEmail(unEmail)