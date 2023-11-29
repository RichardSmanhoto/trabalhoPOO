from classes import vendas
from classes import clientes
from classes import produtos

import sqlite3

database = sqlite3.connect('./database/AutoPecas.db')
cursor = database.cursor()


# !!!!!!! TESTES !!!!!!!
user = clientes.Clientes('Richard', '001')
user.CriarCliente()
print("sucesso")