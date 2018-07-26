# 03_create_data_sql.py
import sqlite3

# Solicitar informações do Funcionário·
print('Cadastrar o Campus')
nome = input('Digite o nome: ')
cidade = input('Digite a cidade: ')

conn = sqlite3.connect('ladoss.db')
cursor = conn.cursor()

# inserindo dados na tabela
query = "INSERT INTO tb_campus (nome, cidade) VALUES ('%s','%s')"%(nome, cidade)
print(query)
cursor.execute(query)

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
