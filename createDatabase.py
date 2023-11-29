'''
Código para criação do banco de dados e todas as tabelas necessarias, caso queira refazer o database, apague na pasta ./database e execute esse código com as alterações
'''

import sqlite3

database = sqlite3.connect('./database/AutoPecas.db')
cursor = database.cursor()

cursor.execute("CREATE TABLE dProdutos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), quantidade INTEGER, precoVenda REAL)")
cursor.execute("CREATE TABLE dClientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), cpf VARCHAR(50))")
cursor.execute("CREATE TABLE fVendas (id INTEGER PRIMARY KEY AUTOINCREMENT, idProduto INTEGER, idCliente INTEGER, data VARCHAR(50), quantidade INTEGER, precoVenda REAL, FOREIGN KEY (idProduto) REFERENCES dProdutos(id), FOREIGN KEY (idCliente) REFERENCES dClientes(id))")

database.commit()
database.close()

# cursor.execute("SELECT * FROM dProdutos")
# print(cursor.fetchall())

print("SUCESS!!!")