import sqlite3

db_file = "tasks.db"

with sqlite3.connect(db_file) as con:

    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks("id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL,
                   descricao TEXT, status BOOLEAN NOT NULL DEFAULT 0") """)

    print(f"Banco de dados {db_file} e tabela task criados com sucesso!")


    
