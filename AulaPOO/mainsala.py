from sala import Salas

def menu():
    print("<- Turmas ->")

    while True:
        opcao = input("Digite a operação desejada:\n A - Cadastrar Turma \n B - Ler Turmas Cadastradas \n X - Sair\n")
        match (opcao):
            case "A":
                codigo_p = input("Digite o código da turma: ")
                lugares_p = input("Digite a capacidade da turma: ")
                tipo_p = input("Digite o tipo da turma (Comum, Informática, Enfermagem ou Estética): ")
                objeto = Salas(codigo_p, lugares_p, tipo_p)
                objeto.inserirTurma()
            case "B":
                objeto_leitura = Salas()
                objeto_leitura.lerDados()
            case "X":
                break
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    menu()