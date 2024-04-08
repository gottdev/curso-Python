# el mayor reto en este proyecto fue comprobar los errores al inicio comprobe con el siguiente codigo

def comprueba_error_numerico(numero):
    while True:
       if numero.isnumeric():
            return numero
       else :
           numero = input( "Error. \ningresa una dato correcto: "  )
           comprueba_error_numerico(numero) 

este si bien me comprobaba el numero entero no los float
de esta forma recorde que se pueden usar las excepciones para este tipo de casos y asi generar una funcion que compruebe los 3 campos

llamando a la misma funcion las veces que sea necesario si el usuario ingresa datos erroneos

para comprobar las cadenas de texto que esten vacias es algo similar 
solo utilizanto la funcion len que esta nos da el tamaño de el str 


eh aprendido que se pueden encontrar muchas soluciones o formas de llegar al mismo resultado 
la forma en la que se explican los temas son muy buenas y claras
