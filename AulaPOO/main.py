from contato import Contato

def menu():
    print("<- Agenda de Contatos ->")

    while True:
        opcao = input("Digite a operação desejada:\n A - Inserir Contato \n B - Ler Contatos \n X - Sair\n")
        match (opcao):
            case "A":
                nome_p = input("Digite seu nome: ")
                email_p = input("Digite seu e-mail: ")
                tel_p = input("Insira seu telefone: ")
                objeto = Contato(nome_p, tel_p, email_p)
                objeto.inserirContato()
            case "B":
                objeto_leitura = Contato()
                objeto_leitura.lerDados()
            case "X":
                break

if __name__ == "__main__":
    menu()