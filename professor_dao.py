import sqlite3

class ProfessorDAO:
    def __init__(self, db_path='banco_escola.db'):
        self.db_path = db_path

    def listar(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, disciplina FROM professor')
        lista = cursor.fetchall()
        conn.close()
        return lista
    

    def salvar(self, id, nome, disciplina):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            if id:  # Atualizar pois um valor para o ID foi informado
                cursor.execute('''
                    UPDATE professor SET nome = ?, disciplina = ? WHERE id = ? 
                ''', (nome, disciplina,  id))
                
            else:  # Inserir
                cursor.execute('''
                    INSERT INTO professor (nome, disciplina) VALUES (?, ?)
                ''', (nome, disciplina))

            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}

        finally:
            conn.close()
            