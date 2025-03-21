class TarjetaCredito:
    # validar tarjeta de creditos
    def __init__(self, numero_tarjeta, saldo_pendiente):
        self.numero_tarjeta = numero_tarjeta
        self.saldo_pendiente = saldo_pendiente

    @staticmethod
    def validar_tarjeta(numero_tarjeta):
        digitos = []
        for d in str(numero_tarjeta):
            digitos.append(int(d))
        digitos.reverse()
        
        # multiplicar por 2 y restar si son mayores a 9
        for i in range(1, len(digitos), 2):
            digitos[i] *= 2
            if digitos[i] > 9:
                digitos[i] -= 9
        suma = sum(digitos)
        return suma % 10 == 0
    
    # consultar saldo pendiente de tarjeta de credito
    @property
    def consultar_saldo_pendiente(self):
        return self.saldo_pendiente
        
    # reducir saldo pendiente de tarjeta de credito
    def reducir_saldo_pendiente(self, monto):
        self.saldo_pendiente -= monto


class Cuenta_Bancaria(TarjetaCredito):
    def __init__(self, saldo, titular, numero_tarjeta, saldo_pendiente):
        self.__saldo = saldo #representa el saldo disponible de la cuenta
        self.__titular = titular #representa el titular de la cuenta
        super().__init__(numero_tarjeta, saldo_pendiente)

    # depositar el dinero en la cuenta si la tarjeta asociada es valida
    def depositar(self, monto):
        if self.validar_tarjeta(self.numero_tarjeta):
            self.__saldo += monto
            return True
        return False
    # Retira dinero de la cuenta si hay suficiente saldo y la tarjeta asociada es válida.
    def retirar(self, monto):
        if self.validar_tarjeta(self.numero_tarjeta) and self.__saldo >= monto:
            self.__saldo -= monto
            return True
        return False
    # retornar saldo actual de la cuenta
    @property
    def consultar_saldo(self):
        return self.__saldo
    #retrorna el nombre del titular de la cuenta
    @property
    def consultar_titular(self):
        return self.__titular
    #Transfiere dinerodesde la cuenta bancaria al saldo pendiente de la tarjeta,
    # siempre que la tarjeta sea válida y haya suficiente saldoen la cuenta.
    def transferir(self, monto):
        if self.validar_tarjeta(self.numero_tarjeta) and self.__saldo >= monto:
            self.__saldo -= monto
            self.reducir_saldo_pendiente(monto)
            return True
        return False

        #ejemplo de uso
if __name__ == "__main__":
    cuenta = Cuenta_Bancaria(10000, "Juan Perez", 5306917181668547,5000)

    #operaciones
    print(f"Saldo de la cuenta: ", cuenta.consultar_saldo)
    print("\n")
    print(f"Titular de la cuenta: ", cuenta.consultar_titular)
    print("\n")
    print(f"Saldo pendiente de la cuenta: ", cuenta.consultar_saldo_pendiente)
    print("\n")
    print(f"depositar saldo: ", cuenta.depositar(5000))
    print("\n")
    print(f"Saldo de la cuenta: ", cuenta.consultar_saldo)
    print("\n")
    print(f"Retirar dinero", cuenta.retirar(1000))
    print("\n")
    print(f"Saldo de la cuenta", cuenta.consultar_saldo)
    print("\n")
    print(f"Transferir dinero: ",cuenta.transferir(2000))
    print("\n")
    print(f"Saldo de la cuenta: ", cuenta.consultar_saldo)
    print("\n")
    print(f"Saldo pendiente: ", cuenta.consultar_saldo_pendiente)
    print("\n")
    print(f"Validar cuenta: ", cuenta.validar_tarjeta(5306917181668547))
    





    
    
