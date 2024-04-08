
def comprueba_error(dato,format): #esta funcion ayuada a comprobar si los datos ingresados son numericos (int, Float) almismo tiempo no permite que la entrada no este vacia
    while True:
        try:
            if format == 1:
                dato= int(dato)
                return dato
            elif format == 2:
                dato = float(dato)
                return dato
            
        
        except ValueError:
            dato = input( "Error. \ningresa una dato correcto: "  )
            comprueba_error(dato , format)

def comprueba_vacio(dato):# comprobamos que las entradas no esten vacias
    while True:
        if dato.strip():
             return dato
        else:
             dato = input( "Error, no puede estar vacio \ningresa una dato correcto: "  )
             comprueba_vacio(dato)

def  comprobar_Imc(IMC): #tome el codigo del ejemplo para complementar la informacion a mostrar
    if IMC >= 0 and IMC <= 15.99 :
        return "Delgadez severa"
    elif IMC >= 16.00 and IMC <= 16.99 :
        return "Delgadez moderada"
    elif IMC >= 17.00 and IMC <= 18.49:
        return "Delgadez leve"
    elif IMC >= 18.50 and IMC <= 24.99 :
        return "Normal"
    elif IMC >= 25.00 and IMC <= 29.99:
        return "Sobrepeso"
    elif IMC >= 30.00 and IMC <= 34.99:
        return "obesidad leve"
    elif IMC >= 35.00 and IMC <= 39.00:
        return"obesidad media"
    elif IMC >= 40.00:
        return "obesidad morbida"

#solicitamos los datos del formulario
nombre = comprueba_vacio ( input( "¿Cual es tu nombre?" )) #solicita el nombre y se asigna a una variable
apellido_paterno = comprueba_vacio ( input( "¿Cual es tu apellido Paterno ?" )) #solicita el apellido paterno y se asigna a una variable
apellido_Materno = comprueba_vacio ( input( "¿Cual es tu apellido Materno ?" )) #solicita el apellido materno y se asigna a una variable
edad = comprueba_error ( input( "¿Cual es tu Edad ?") , 1) #solicita la edad y se asigna a una variable
peso = comprueba_error ( input( "ingresa tu peso en Kilograsmos: " ) , 2)  #solicita el peso y se asigna a una variable
estatura = comprueba_error ( input( "ingresa tu estatura en Metros: " ) , 2)  #solicita la estatura y se asigna a una variable

imc = peso / ( estatura ** 2 ) #se raliza la operacion para calcular el "IMC" y se agrega a una variable|

#imprimimos los datos recopilados
print("----DATOS GENERALES----" )
print( nombre.title(), apellido_paterno.title(), apellido_Materno.title()) #se utiliza la funcion title para el primer caracter ponerlo en mayuscula
print( "edad: %s años"  %(edad) ) #utilizo una forma de las que se cuenta en python para concatenar un int en una cadena de texto sin la clasica de convertirlo a un str 
print("tu indice de masa corporal es: " , "{:.2f}".format(imc)) # solo tomo en cuenta las 2 decimales del float 
print("tines un indice de masa corporal(IMC) : " , comprobar_Imc(imc) )    


