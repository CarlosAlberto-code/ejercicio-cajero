# 1ra Evaluación - DevSecOps  (2da parte)

Crea un programa tanto en Java como en Python, de un cajero automático. Al iniciar el programa deberá pedir el siguiente pin: “1235” para autenticar. Si está mal, deberá pedirlo máximo 3 veces. Si pasando esas 3 vez el pin no es correcto, el programa deberá terminarse. Si es correcto mostrará un mensaje de bienvenida con tu nombre y mostrando 3 opciones: 

* Consultar saldo 
* Retirar saldo 
* Histórico de Movimientos 

El saldo inicial deberá ser de 1,000 pesos. Cada que se retire saldo, el saldo inicial deberá ajustarse. Si se llega a 0 deberá mostrar un mensaje de que no se tienen fondos suficientes y una opción para continuar al menú o salir de la aplicación. Cada opción: 

* Consultar saldo 
* Retirar saldo 
* Histórico de Movimientos  

Deberá tener la opción de regresar al menú principal o salir. 

La opción de histórico deberá mostrar la fecha del movimiento, hora, minuto y segundo de cuanto fue el retiro hecho así como del saldo que se tenia anteriormente

# Requisitos 🔧
* Java version 7 o superior.
* Python 2/3

# Instrucciones Java
* Clonar el repositorio
* Acceder a la carpeta Cajero Java con el comando ```cd "Cajero Java"```
* Compilar todos los archivos .java con el comando ``` javac *.java ```
* Ejecutar el archivo principal: ``` java Cajero ```
* Enjoy!
