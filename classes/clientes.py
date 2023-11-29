import sqlite3

database = sqlite3.connect('./database/AutoPecas.db')
cursor = database.cursor()


class Clientes:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def CriarCliente(self):
        cursor.execute(f"INSERT INTO dClientes (nome, cpf) VALUES ('{self.nome}', '{self.cpf}')")
        database.commit()
        database.close()

