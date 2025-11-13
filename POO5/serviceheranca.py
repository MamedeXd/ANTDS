from service import Conta

class ContaPoupanca(Conta):
    
    def depositar(self, valor_deposito):
        if valor_deposito <= 0 or valor_deposito == None:
            print("Valor inválido!")
        else:
            valor_rendimento = valor_deposito * 0.05
            self._saldo = self._saldo + valor_deposito + valor_rendimento
            print("Depósito realizado com sucesso!")