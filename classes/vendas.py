import sqlite3

database = sqlite3.connect('./database/AutoPecas.db')
cursor = database.cursor()


class Vendas:
    def __init__(self, idProduto, idCliente, data, quantidade, precoVenda):
        self.idProduto = idProduto
        self.idCliente = idCliente
        self.data = data
        self.quantidade = quantidade
        self.precoVenda = precoVenda


# Como eu pensei em puxar os dados de clientes no processo de RealizarVenda() você irá verificar o cpf da moça na tabela dClientes. Caso exista, voce pega o id e insere na tabela fvendas, se nao existir você retorna um erro "usuário inexistente". 