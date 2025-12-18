class Produto:
    def __init__(self, id=None, nome="", descricao="",preco="",qtd_estoque="", categoriaID=""):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao 
        self.__preco = preco
        self.__qtd_estoque = qtd_estoque
        self.__categoriaID = categoriaID
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, valor):
        if valor is None or isinstance(valor, int):
            self.__id = valor
        else:
            raise ValueError("ID deve ser inteiro ou None")
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__nome = valor.strip()
        else:
            raise ValueError("Nome deve ser string não vazia (máx. 100 caracteres)")

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, valor):
        if isinstance(valor, str) and len(valor) <= 500:
            self.__descricao = valor.strip()
        else:
            raise ValueError("Descrição deve ser string (máx. 500 caracteres)")

    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, valor):
        self.__preco = valor.strip()

    @property
    def qtd_estoque(self):
        return self.__qtd_estoque
    @qtd_estoque.setter
    def qtd_estoque(self,valor):
        self.__qtd_estoque = valor.strip()
    
    @property
    def categoriaID(self):
        return self.__categoriaID
    @categoriaID.setter
    def categoriaID(self,valor):
        self.__categoriaID = valor.strip()

