import sqlite3

conn = sqlite3.connect('ladoss.db')
cursor = conn.cursor()

nome = 'joyce'
novo_email = 'joyce@mail'

# alterando os dados da tabela
cursor.execute("""
UPDATE tb_funcionario
SET email = ?
WHERE nome = ?
""", (novo_email, nome))

conn.commit()

print('Dados atualizados com sucesso.')

conn.close()
