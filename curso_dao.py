from db_config import get_connection

class CursoDAO:
    def __init__(self, db_path='banco_escola.db'):
        self.db_path = db_path

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome_curso, duracao  FROM curso')
        lista = cursor.fetchall()
        conn.close()
        return lista
    

   