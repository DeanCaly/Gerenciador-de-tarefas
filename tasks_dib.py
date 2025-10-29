import sqlite3

DATABASE = "tasks.db"

def add_tasks(titulo: str, descrissao: str) -> None: 
    
    sql_insert = """INSERT INTO tasks (titulo, descrissao, status) (VALUES ?, ?)"""
    data_to_insert = (titulo, descrissao)

    #separação entre código a ser inserido e conexão com o banco de dados

    with sqlite3.connect(DATABASE) as con:
        cursor = con.cursor()
        cursor.execute(sql_insert, data_to_insert)

    print(f"Tarefa {titulo} adicionada com sucesso")


def get_all_tasks():
    sql_query = """SELECT * FROM tasks"""

    with sqlite3.connect(DATABASE) as con:

        con.row_factory = sqlite3.Row

        cursor = con.cursor()
        res = cursor.execute(sql_query)
        all_tasks = res.fetchall()


    return all_tasks

def update_task_status(task_id: int, new_status: int) -> None:
    sql_insert = "UPDATE tasks SET status = ? WHERE id = ?"
    data_to_insert = (new_status, task_id)

    with sqlite3.connect(DATABASE) as con:

        cursor = con.cursor()
        cursor.execute(sql_insert, data_to_insert)

        print("Status da tarefa modificado com sucesso")

    
def delete_task(task_id) -> None:
    sql_insert = "DELETE FROM tasks WHERE titulo = ?"
    data_to_insert = task_id

    with sqlite3.connect(DATABASE) as con:
        cursor = con.cursor()
        cursor.execute(sql_insert, data_to_insert)

        print(f"Tarefa com id {task_id} deletada com sucesso")