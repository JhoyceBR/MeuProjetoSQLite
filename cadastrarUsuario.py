# 03_create_data_sql.py
import sqlite3

# Solicitar informações do Funcionário·
print('Cadastrar o Funcionário')
nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
cpf = input('Digite a CPF: ')
email = input('Digite a e-mail: ')

conn = sqlite3.connect('ladoss.db')
cursor = conn.cursor()

# inserindo dados na tabela
query = "INSERT INTO tb_funcionario (nome, idade, cpf, email) VALUES ('%s', %d, '%s', '%s')"%(nome, idade, cpf, email)
print(query)
cursor.execute(query)

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
