def menu():
    
    """Funcion que Muestra el Menu"""
    
    print(
    
    """
    Menu:
    
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Salir
    """
    
    )

def Calculadora():
    
    """Funcion para calcular opciones aritmeticas"""
    
    menu()
    opc = int(input("Seleccione Opcion:"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese Numero:"))
        y = int(input("Ingrese otro Numero: "))
        if (opc==1): 
            print"La suma es:", x+y
            opc = int(input("Seleccione Opcion:"))
        elif (opc==2):
            print"La resta es:", x-y
            opc = int(input("Seleccione Opcion:"))
        elif (opc==3):
            print"La multiplicacion es:", x*y
            opc = int(input("Seleccione Opcion:"))
        elif (opc==4):
            try:
                print"La division es:", float(x%y)
                opc = float(input("Seleccione Opcion:"))
            except ZeroDivisionError:
                print"No se permite la division entre 0"
                opc = float(input("Seleccione Opcion:"))
Calculadora()