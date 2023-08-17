import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='gabriel',
    password='root',
    database='bdyoutube',
)

cursor = conexao.cursor()

#CRUD

#CREATE
nome_produto = "chocolate"
valor = 11
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() #edita o banco de dados

#READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() #ler o banco de dados
print(resultado)

#UPDATE
valor = 6
nome_produto = "chocolate"
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}" '
cursor.execute(comando)
conexao.commit()

#DELETE
nome_produto = "chocolate"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()