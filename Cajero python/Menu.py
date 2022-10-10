class Menu:

    def mostrar(self):
        print("\nSelecciona una opcion")
        print("1.- Ver saldo actual")
        print("2.- Ver historico de movimientos")
        print("3.- Retirar saldo")
        print("4.- Salir")
        return self.validadorDeEntrada()

    def validadorDeEntrada(self):
        error = True
        while error:
            entrada = raw_input("Selecciona una opcion: ")
            if entrada.isdigit():
                if int(entrada) <= 4 and int(entrada) >= 1:
                    error = False
                else:
                    print("\nOpcion no valida, ingresa un valor entre 1 y 4.")
            else:
                print("\nOpcion no valida, ingresa de nuevo")
        
        return entrada