import sqlite3

class CursoDAO:
    def __init__(self, db_path='banco_escola.db'):
        self.db_path = db_path

    def listar(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome_curso, duracao  FROM curso')
        lista = cursor.fetchall()
        conn.close()
        return lista
    

   