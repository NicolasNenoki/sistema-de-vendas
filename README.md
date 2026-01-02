# Sistema de Vendas - API REST com Flask

Uma API RESTful simples e eficiente para gerenciamento de categorias e produtos em um sistema de vendas. Desenvolvida com **Flask** (Python), conectada a um banco de dados **MySQL**.

## Funcionalidades

### Categorias
- Listar todas as categorias (`GET /categorias`)
- Buscar categoria por ID (`GET /categorias/<id>`)
- Cadastrar nova categoria (`POST /categorias`)
- Remover categoria (`DELETE /categorias/<id>`)

### Produtos
- Listar todos os produtos (`GET /produtos`)
- Buscar produto por ID (`GET /produtos/<id>`)
- Cadastrar novo produto (`POST /produtos`)
- Remover produto (`DELETE /produtos/<id>`)

## Tecnologias Utilizadas
- **Flask** - Framework web leve em Python
- **Gunicorn** - Servidor WSGI para produção
- **MySQL** - Banco de dados relacional
- **mysql-connector-python** - Conector oficial MySQL para Python
- **Railway** - Plataforma de deploy (hospedagem atual)

## Deploy
A aplicação está atualmente hospedada no Railway (disponivel até dia 17/01/2026) e acessível em:
https://sistema-de-vendas-nicolasnenoki.up.railway.app

## Autor
Desenvolvido por Nicolas Nenoki, no curso de Python com Frameworks do SENAI SP.
