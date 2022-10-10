from Autenticador import Autenticador
from Menu import Menu
from Saldo import Saldo 

class Cajero:

    def iniciar(self):
        if Autenticador().esValido():
            saldo = Saldo()
            print("\n Usuario Autenticado \n")
            continuar = True
            while continuar:

                opcion = Menu().mostrar()
                if opcion == "1":
                    saldo.consultarSaldoActual()
                if opcion == "2":
                    saldo.consultarHistorial()
                if opcion == "3":
                    saldo.retirar()
                if opcion == "4":
                    continuar = False
            print("\n Adios!")

        else:
            print("\n Se terminaron el numero de intentos, prueve nuevamente mas tarde")