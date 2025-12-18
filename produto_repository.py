from conexao import Conexao

class ProdutoRepository:
    def __init__(self):
        self.conexao = Conexao()

    def find_all(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("""SELECT ProdutoID as id, Nome as nome, Descricao as descricao, Preco as preco, QuantidadeEstoque as qtd_estoque, CategoriaID as categoriaID 
        FROM Produto ORDER BY ProdutoID""")
        return cursor.fetchall()

    def find_by_id(self, produto_id):
            cursor = self.conexao.get_cursor()
            cursor.execute(
                """SELECT ProdutoID as id, Nome as nome, Descricao as descricao, Preco as preco, QuantidadeEstoque as qtd_estoque, CategoriaID as categoriaID 
         FROM Produto WHERE ProdutoID = %s""",
                (produto_id,)
            )
            return cursor.fetchone()

    def create(self, nome, descricao, preco, qtd_estoque, categoria_id):
        """Insere novo registro (ID auto-increment)."""
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute(
            "INSERT INTO Produto (Nome, Descricao, Preco, QuantidadeEstoque, CategoriaID) "
            "VALUES (%s, %s, %s, %s, %s);",
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

    # def update(self, produto_id, nome, descricao, preco, qtd_estoque, categoria_id):
    #     # """Atualiza registro existente."""
    #     # cursor = None
    #     # try:
    #     #     cursor = self.conexao.get_cursor()
    #     #     cursor.execute(
    #     #         "UPDATE Produto SET Nome = %s, Descricao = %s WHERE CategoriaID = %s",
    #     #         (nome, descricao, categoria_id)
    #     #     )
    #     #     self.conexao.get_conexao().commit()
    #     #     return cursor.rowcount > 0
    #     # except Exception as e:
    #     #     print(f"Erro ao atualizar categoria {categoria_id}: {e}")
    #     #     self.conexao.get_conexao().rollback()
    #     #     return False
    #     # finally:
    #     #     if cursor:
    #     #         cursor.close()

    def delete(self, produto_id):
        """Remove registro pelo ID."""
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
        """Fecha conexão do repositório."""
        self.conexao.fechar_conexao()


# Instância global
repo = ProdutoRepository()

# Teste funcionando

produtos = repo.find_all()
print("Produto encontradas:", produtos)
    
pro = repo.find_by_id(1)
print("Produto 1:", pro)