import datetime

class Saldo(object):
    monto = int()
    movimientos = []

    def __init__(self):
        self.monto = 1000

    def consultarSaldoActual(self):
        print ("\n--- Tu saldo actual es de: " + str(self.monto) + " \n")

    def consultarHistorial(self):
        print ("\n-- Historial de movimientos")
        for movimiento in self.movimientos:
            print(movimiento)

    def mensajeDeExito(self):
        print ("\n-- Operacion realizada con exito -- \n")

    def registrarOperacion(self, montoRetidado):
        s1 = "--Fecha: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        s2 = " Monto retirado: " + str(montoRetidado)
        s3 = " Saldo Anterior: " + str(self.monto) + "\n"
        s4 = s1 + s2 + s3
        self.movimientos.append(s4)
        self.mensajeDeExito()

    def disminuirSaldo(self, montoARetirar):
        self.monto -= int(montoARetirar)

    def solicitarMontoARetirar(self):
        error = True
        while error:
            print("\n-- Denominaciones disponibles: 50, 100, 200 y 500")
            print("-- Saldo actual: " + str(self.monto))
            montoDeRetiro = raw_input("-- Ingresa el monto a retirar: ")
            if montoDeRetiro.isdigit():
                if int(montoDeRetiro) % 50 == 0:
                    self.registrarOperacion(montoDeRetiro)
                    self.disminuirSaldo(montoDeRetiro)
                    error = False
                else:
                    print ("-- No existen billetes de esa dominacion, no podemos darte esa cantidad")
            else:
                print ("-- No es una entrada valida")

    def retirar(self):
        if self.monto > 0:
            self.solicitarMontoARetirar()
        else:
            print("\n-- Saldo insuficiente")