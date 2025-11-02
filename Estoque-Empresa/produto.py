class Produto:
    def __init__(self, nome_p, codigo_p):
        self.nome = nome_p
        self.codigo = codigo_p
    
    def verDados(self, codigo=None):
        if codigo == self.codigo:
            print(f"O produto selecionado é {self.nome}.")
        else:
            print("Código incorreto ou inexistente.")

Parafuso = Produto("Parafuso", "1a2b")
Parafuso.verDados("1a2b")
Parafuso = Produto("Parafuso", "1a2b")
Parafuso.verDados("1a2")