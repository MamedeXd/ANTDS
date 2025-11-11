class Salas:

    def __init__(self, codigo_p="", lugares_p="", tipo_p="Comum"):
        self.tipos     = ["Comum", "Informática", "Enfermagem", "Estética"]
        self.codigo    = codigo_p
        self.lugares   = lugares_p
        self.tipo      = tipo_p

    
    def validaTipo(self, tipo_digitado):
        if tipo_digitado in self.tipos:
            self.tipo = tipo_digitado
            return True
        else:
            return False        
    
    def inserirTurma(self):
        if self.validaTipo(self.tipo) == True:
            with open("salas.txt", "a") as arquivo:
                arquivo.write(f"{self.codigo} - {self.lugares} - {self.tipo} \n")
            print("Dados inseridos com sucesso!")
        else:
            print("Tipo de turma inválido!")
    
    def lerDados(self):
        lista_dados = []
        with open("salas.txt", "r") as arquivo:
            lista_dados = arquivo.readlines()
        print(lista_dados)