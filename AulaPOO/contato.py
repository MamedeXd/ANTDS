class Contato:

    def __init__(self, nome_p="", telefone_p="", email_p=""):
        self._id    = None
        self._nome  = nome_p
        self._tel   = telefone_p
        self._email = email_p
    
    def inserirContato(self):
        # arquivo = open("agenda.txt", "a")
        # arquivo.write(f"{self._nome, self._email, self._tel}")
        # arquivo.close()

        with open("agenda.txt", "a") as arquivo:
            arquivo.write(f"{self._nome} - {self._email} - {self._tel} \n")
        print("Dados inseridos com sucesso!")
    
    def lerDados(self):
        lista_dados = []
        with open("agenda.txt", "r") as arquivo:
            lista_dados = arquivo.readlines()
        print(lista_dados)