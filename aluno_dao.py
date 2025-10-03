import sqlite3

class AlunoDAO:
    def __init__(self, db_path='banco_escola.db'):
        self.db_path = db_path

    def listar(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, idade, cidade FROM aluno')
        lista = cursor.fetchall()
        conn.close()
        return lista
    

    def salvar(self, id, nome, idade, cidade):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            if id:  # Atualizar pois um valor para o ID foi informado
                cursor.execute('''
                    UPDATE aluno SET nome = ?, idade = ?, cidade = ? WHERE id = ? 
                ''', (nome, idade, cidade, id))
                
            else:  # Inserir
                cursor.execute('''
                    INSERT INTO aluno (nome, idade, cidade) VALUES (?, ?, ?)
                ''', (nome, idade, cidade))

            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}

        finally:
            conn.close()
            

    def buscar_por_id(self, id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, idade, cidade FROM aluno WHERE id = ?', (id,))
        registro = cursor.fetchone() # retorna o registro selecionado
        conn.close()
        return registro            
    
    
    def remover(self, id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM aluno WHERE id = ?', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()