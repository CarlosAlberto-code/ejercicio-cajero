from Autenticador import Autenticador
from Saldo import Saldo 

if Autenticador().esValido():
    print("Usuario Autenticado")
else:
    print("Se terminaron el numero de intentos, prueve nuevamente mas tarde")