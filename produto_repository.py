from conexao import Conexao

class ProdutoRepository:
    def __init__(self):
        self.conexao = Conexao()

    def find_all(self):
        cursor = self.conexao.get_cursor()
        try:
            cursor.execute("""SELECT ProdutoID as id, Nome as nome, Descricao as descricao, 
                             Preco as preco, QuantidadeEstoque as qtd_estoque, CategoriaID as categoriaID 
                             FROM Produto ORDER BY ProdutoID""")
            return cursor.fetchall()
        finally:
            cursor.close()

    def find_by_id(self, produto_id):
        cursor = self.conexao.get_cursor()
        try:
            cursor.execute(
                """SELECT ProdutoID as id, Nome as nome, Descricao as descricao, Preco as preco, 
                QuantidadeEstoque as qtd_estoque, CategoriaID as categoriaID 
                FROM Produto WHERE ProdutoID = %s""",
                (produto_id,)
            )
            return cursor.fetchone()
        finally:
            cursor.close()

    def create(self, nome, descricao, preco, qtd_estoque, categoria_id):
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute(
                "INSERT INTO Produto (Nome, Descricao, Preco, QuantidadeEstoque, CategoriaID) "
                "VALUES (%s, %s, %s, %s, %s)",
                (nome, descricao, preco, qtd_estoque, categoria_id)
            )
            self.conexao.get_conexao().commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Erro ao criar produto: {e}")
            self.conexao.get_conexao().rollback()
            return None
        finally:
            if cursor:
                cursor.close()

    def delete(self, produto_id):
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute("DELETE FROM Produto WHERE ProdutoID = %s", (produto_id,))
            self.conexao.get_conexao().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao deletar Produto {produto_id}: {e}")
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def fechar_conexao(self):
        self.conexao.fechar_conexao()