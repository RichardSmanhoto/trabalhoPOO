import sqlite3

database = sqlite3.connect('./database/AutoPecas.db')
cursor = database.cursor()

class Produtos:
    def __init__(self, nome: str, precoVenda: float, quantidade: int):
        self.nome = nome
        self.precovenda = precoVenda
        self.quantidade = quantidade

    def cadastroProduto(self):
        cursor.execute(f"INSERT INTO dProdutos (nome, precoVenda, quantidade) VALUES ('{self.nome}', {self.precovenda}, {self.quantidade})")
        database.commit()

    def consultarProdutos(self):
        cursor.execute(f"SELECT * FROM dProdutos")
        print(cursor.fetchall())

