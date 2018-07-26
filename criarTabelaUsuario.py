# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('ladoss.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE tb_funcionario (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL
);
""")
print('Funcionário: Tabela criada com sucesso.')

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE tb_campus (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cidade TEXT NOT NULL
);
""")
print('Campus: Tabela criada com sucesso.')

# desconectando...
conn.close()
