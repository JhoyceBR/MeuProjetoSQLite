# 06_read_data.py
import sqlite3

conn = sqlite3.connect('ladoss.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM tb_campus;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
