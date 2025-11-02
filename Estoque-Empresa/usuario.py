class Usuario:
    def __init__(self, nome_u, cpf_u, senha_u):
        self.nome = nome_u
        self.cpf = cpf_u
        self.senha = senha_u
    
    def verDados(self, senha):
        if senha != self.senha:
            print("Senha inválida. Tente novamente.")
        else:
            print(f"Bem-vindo(a) {self.nome}.")

Gabriel = Usuario("Gabriel", "123.456.789-10", "user1")
Gabriel.verDados("user1")
Gabriel = Usuario("Gabriel", "123.456.789-10", "user1")
Gabriel.verDados("user2")