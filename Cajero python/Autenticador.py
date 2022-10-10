class Autenticador :
    PIN = "123"
    intentos = 3
    def  esValido(self) :
        autenticado = False
        while True :
            entrada = raw_input("-- Ingresa tu PIN para acceder al sistema: ")
            if (entrada==Autenticador.PIN) :
                autenticado = True
            else :
                self.intentos -= 1
            if((self.intentos > 0 and not autenticado) == False) :
                    break
        return autenticado