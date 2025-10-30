#Importação - dizer de qtal arquivo vem o recurso
#from arquivo import recurso
from cliente import Cliente

class Conta:
    def __init__(self, saldo_p, num_conta_p, agencia_p):
        self.saldo: float = saldo_p
        self.numero_conta: int = num_conta_p
        self.agencia: str = agencia_p
        self.cliente_banco: Cliente = None
    
    def verSaldo(self):
        print(f"O saldo atual é R${self.saldo}")
    
    def sacar(self, valor_saque):
        if valor_saque < 0:
            print("Valor de saque inválido!")
        elif self.saldo < valor_saque:
            print("Saldo Insuficiente!")
        else:
            self.saldo = self.saldo - valor_saque
            print("Saque realizado com sucesso!")
    
    def depositar(self, valor_deposito):
        if valor_deposito <= 0:
            print("Valor inválido!")
        else:
            self.saldo = self.saldo + valor_deposito
            print("Depósito realizado com sucesso!")

cc1 = Conta()
cc1.depositar(69.96)
cc2 = Conta()
cc2.depositar(99)
cc1.verSaldo()
cc2.verSaldo()