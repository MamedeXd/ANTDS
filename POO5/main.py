from service import Conta
from service import ContaPoupanca

if __name__ == "__main__":
    objetoConta = Conta("02112", 100.0, "Gabriel M.")
    print("<-- Conta Comum -->")
    objetoConta.verSaldo()
    objetoConta.depositar(50)
    objetoConta.verSaldo()
    print("<-- Conta Poupanca -->")
    objetoPoupanca = ContaPoupanca("012210", 100.0, "Gabriela M.")
    objetoPoupanca.verSaldo()
    objetoPoupanca.depositar(50)
    objetoPoupanca.verSaldo()