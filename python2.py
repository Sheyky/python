#coding=utf-8

def menu():

    """ Menu para el juego C: """
    
    print(

       """
       Menu:
       1) Jugar
       2) Salir
       """ 
    )
def introduccion():
    
    """ Introduccion al juego"""

    menu()
    opc = int(input("Elije una opcion: "))
    if(opc==1):
        name=raw_input("Cual es tu nombre?: ")
        
        print ("Hola {} aqui empieza esta pequeña prueba de aventura basada en texto.".format(name))
    
    else:
        quit()

def continuacion():
    """ Seleccion de clase"""
    
    introduccion()
    
    mago="Mago"
    caballero="Caballero"
    parguelas="Parguelas"
    comunista="Comunista"
   
    print("""
            1) Mago
            2) Caballero
            3) Parguelas
            """)
    clase = int(input("""
    Selecciona una clase: 
            """))
    if(clase==1):
            print("Has escogido ser un {} , son poderosos hechizeros que basan su fortaleza en la inteligencia y el ataque desde la distancia.".format(mago))
            return True
    elif(clase==2):
            print("Has escogido ser un {} , son defensores que utilizan armaduras pesadas y escudos para defender a sus aliados.".format(caballero))
            return True
    elif(clase==3):
            print("Has escogido ser un {} , son pues eso , parguelas.".format(parguelas))
            return True
    elif(clase==4):
            print("Has escogido ser un {} , SON DIOSES!.".format(comunista))
            return True
    else:
        print("Esa clase no existe, elije otra.")
	return False

respuesta=False        
while not respuesta:
	respuesta=continuacion()  

# Al pulsar enter , error.
# Al introducir caracter no numerico , error.
