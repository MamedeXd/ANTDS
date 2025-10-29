#Programação Orientada a Objetos
#Classes - Modelo/ representação de um conjunto de características em comum


class Cliente:
    def __init__(self, nome_p, cpf_p, email_p, senha_p): #Inicia os atributos
        self.nome = nome_p
        self.cpf = cpf_p
        self.email = email_p
        self.senha = senha_p
    
    def verDados(self, senha=None):
        if senha == self.senha:
            print(f"Os dados: {self.nome} - {self.cpf} - {self.email}")
        else:
            print("Senha Inválida!")

cGabriel = Cliente("Gabriel", "123.xxx.xxx-xx", "grm@gmail.com", "admin") #Criando um objeto do tipo Cliente
cGabriel.verDados("admin")

cPaulo = Cliente("Paulo", "012.xxx.xxx-xx", "p@gmail.com", "admin123")
cPaulo.verDados("admin")

cWinike = Cliente("Winike", "987.xxx.xxx-65", "wk@gmail.com", "musculoso")
cWinike.verDados("musculoso")

cDavi = Cliente("Davi", "696.969.696-69", "da@gmail.com", "fininho")
cDavi.verDados("fininho")