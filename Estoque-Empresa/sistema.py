
from usuario import Usuario
from produto import Produto

class Estoque:
    def __init__(self, usuario_s, produto_s, quantidade_s):
        self.usuario: Usuario = usuario_s
        self.produto: Produto = produto_s
        self.quantidade: int = quantidade_s
    
    def verQuantidade(self):
        print(f"A quantidade atual no estoque é {self.quantidade}.")
    
    def adicionar(self, valor_adicionar):
        if valor_adicionar < 0:
            print("Valor inválido.")
        else:
            self.quantidade = self.quantidade + valor_adicionar
            print(f"Produto adicionado ao estoque! O estoque atual é de {self.quantidade}.")
    
    def remover(self, valor_remover):
        if valor_remover > self.quantidade:
            print("O valor é maior que o estoque atual.")
        else:
            self.quantidade = self.quantidade - valor_remover
            print(f"Quantidade removida do estoque! O estoque atual é de {self.quantidade}.")

atual = Estoque(None, None, "10")
atual.verQuantidade()
adi1 = Estoque(None, None, 10)
adi1.adicionar(10)
sub1 = Estoque(None, None, 10)
sub1.remover(5)