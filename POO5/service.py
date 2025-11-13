class Conta:
    
    def __init__(self, numero, saldo, cliente):
        self._numero_conta = numero
        self._saldo = saldo
        self._cliente = cliente
    
    def sacar(self, valor_saque):
        self._saldo = self._saldo - valor_saque
        print("Saque realizado com sucesso!")
    
    def depositar(self, valor_deposito):
        if valor_deposito <= 0 or valor_deposito == None:
            print("Valor inválido!")
        else:
            self._saldo = self._saldo + valor_deposito
            print("Depósito realizado com sucesso!")
    
    def verSaldo(self):
        print(f"O saldo atual é R${self._saldo}")