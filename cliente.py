#Se crea la clase cliente, con los atributos para generar la base de cliente que nos interesa
#Pensado para luego generar codigo que envie mails a los clientes segun sus intereses

class Cliente:
    def __init__(self, nombre, apellido, nro_documento, edad,categoria_interes):
        self.documento = nro_documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.categoria_interes = categoria_interes 
    
    def __str__(self):
        return self.nombre + " " + self.apellido
    
    def interes(self):
        print ("Al cliente",self.apellido,"le interesa la categoria",self.categoria_interes)

    