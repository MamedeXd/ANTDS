from conta import Conta
from cliente import Cliente

def menu():
    objetoCliente = Cliente("Kim Jisoo", "103.103.103-10", "jisooya@gmail.com", "kimjisooya")
    objetoConta = Conta(100, "0103-1", "103", objetoCliente)
    while True:
        print("="*50)
        print("BANCO SANTANDRE")
        opcao = input("Digite: \n E = Criar Conta \n A = Sacar \n B = Depositar \n C = Ver Saldo \n X = Sair")
        match (opcao.upper()):
            case "A":
                print(objetoConta)
                print(objetoCliente)
                valor_saque = float(input("Informe o valor do saque em R$: "))
                objetoConta.sacar(valor_saque)
            case "B":
                valor_deposito = float(input("Informe o valor do depósito em R$: "))
                objetoConta.depositar(valor_deposito)
            case "C":
                objetoConta.verSaldo()
            case "X":
                break
            case "E":
                v_saldo = float(input("Depósito Inicial: R$"))
                v_numero = random.randint(100, 20000)
                v_agencia = input("Informe a agência: ")
                objetoConta = Conta(v_saldo, v_numero, v_agencia, objetoCliente)

if __name__ == "__main__":
    menu()