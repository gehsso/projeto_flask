import sqlite3

class TurmaDAO:
    def __init__(self, db_path='banco_escola.db'):
        self.db_path = db_path

    def listar(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT turma.id, turma.semestre, curso.nome_curso, professor.nome,professor.disciplina
            FROM turma
            JOIN curso ON turma.curso_id = curso.id
            JOIN professor ON turma.professor_id = professor.id
        ''')
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, semestre, curso_id, professor_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            if id:
                cursor.execute('''
                    UPDATE turma SET semestre = ?, curso_id = ?, professor_id = ? WHERE id = ?
                ''', (semestre, curso_id, professor_id, id))
            else:
                cursor.execute('''
                    INSERT INTO turma (semestre, curso_id, professor_id) VALUES (?, ?, ?)
                ''', (semestre, curso_id, professor_id))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, semestre, curso_id, professor_id FROM turma WHERE id = ?', (id,))
        turma = cursor.fetchone()
        conn.close()
        return turma
    
    
    def remover(self, id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM turma WHERE id = ?', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()    

#https://chatgpt.com/c/687adfa0-3308-800f-aeba-0fea3c518393