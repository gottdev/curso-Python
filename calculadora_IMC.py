nombre = input( "¿Cual es tu nombre?" ) #solicita el nombre y se asigna a una variable
apellido_paterno = input( "¿Cual es tu apellido Paterno ?" ) #solicita el apellido paterno y se asigna a una variable
apellido_Materno = input( "¿Cual es tu apellido Materno ?" ) #solicita el apellido materno y se asigna a una variable
edad = int(input( "¿Cual es tu Edad ?" )) #solicita la edad y se asigna a una variable
peso = float(input( "ingresa tu peso en Kilograsmos: " )) #solicita el peso y se asigna a una variable
estatura = float(input( "ingresa tu estatura en Metros: " )) #solicita la estatura y se asigna a una variable

imc = peso / ( estatura ** 2 ) #se raliza la operacion para calcular el "IMC" y se agrega a una variable

print("tu indice de masa corporal es: ", imc)

