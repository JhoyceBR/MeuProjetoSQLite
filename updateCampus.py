import sqlite3

conn = sqlite3.connect('ladoss.db')
cursor = conn.cursor()

nome_campus = 'Guarabira'
novo_nome = 'IFPB - GBA'

# alterando os dados da tabela
cursor.execute("""
UPDATE tb_campus
SET nome = ?
WHERE nome = ?
""", (novo_nome, nome_campus))

conn.commit()

print('Dados atualizados com sucesso.')

conn.close()
