from conexao import Conexao

class CategoriaRepository:
    def __init__(self):
        self.conexao = Conexao()

    def find_all(self):
        cursor = self.conexao.get_cursor()
        try:
            cursor.execute("SELECT CategoriaID as id, Nome as nome, Descricao as descricao FROM Categoria ORDER BY CategoriaID")
            return cursor.fetchall()
        finally:
            cursor.close()

    def find_by_id(self, categoria_id):
        cursor = self.conexao.get_cursor()
        try:
            cursor.execute(
                "SELECT CategoriaID as id, Nome as nome, Descricao as descricao FROM Categoria WHERE CategoriaID = %s",
                (categoria_id,)
            )
            return cursor.fetchone()
        finally:
            cursor.close()

    def create(self, nome, descricao=""):
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute(
                "INSERT INTO Categoria (Nome, Descricao) VALUES (%s, %s)",
                (nome, descricao)
            )
            self.conexao.get_conexao().commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Erro ao criar categoria: {e}")
            self.conexao.get_conexao().rollback()
            return None
        finally:
            if cursor:
                cursor.close()

    def update(self, categoria_id, nome, descricao=""):
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute(
                "UPDATE Categoria SET Nome = %s, Descricao = %s WHERE CategoriaID = %s",
                (nome, descricao, categoria_id)
            )
            self.conexao.get_conexao().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao atualizar categoria {categoria_id}: {e}")
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def delete(self, categoria_id):
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute("DELETE FROM Categoria WHERE CategoriaID = %s", (categoria_id,))
            self.conexao.get_conexao().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao deletar categoria {categoria_id}: {e}")
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def fechar_conexao(self):
        self.conexao.fechar_conexao()