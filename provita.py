import mysql.connector

def create_database():
    conexao_db = mysql.connector.connect(user='root', password='Dodeges32*', host='127.0.0.1')
    cursor_db = conexao_db.cursor()
    cursor_db.execute("CREATE DATABASE IF NOT EXISTS db_loja_3")
    cursor_db.close()
    conexao_db.close()
    print('\nConexão db fechada.')

def create_connection():
    con = mysql.connector.connect(user='root', password='Dodeges32*', host='127.0.0.1', database='db_loja_3')
    print('Conexão:', con)
    return con

def close_connection(con, cursor):
    cursor.close()
    con.close()
    print('\nConexão fechada.')

def create_table_produto():
    sql = """ CREATE TABLE IF NOT EXISTS tb_produto(
    idt INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL UNIQUE,
    preco DECIMAL(9,2) NOT NULL,
    dta_validade DATE NULL,
    PRIMARY KEY (idt)
    )"""
    cursor.execute(sql)

def create_table_clientes():
    sql = """ CREATE TABLE IF NOT EXISTS tb_clientes(
    idt INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL UNIQUE,
    telefone VARCHAR(15) NULL,
    data_nascimento DATE NULL,
    PRIMARY KEY (idt)
    )"""
    cursor.execute(sql)

def insert_produto():
    nome = input('Nome do produto: ')
    preco = float(input('Preço: '))
    dta_validade = input('Data de validade (aaaa-mm-dd, opcional): ')
    sql = f"""INSERT INTO tb_produto (nome, preco, dta_validade)
              VALUES ('{nome}', {preco}, '{dta_validade}')"""
    cursor.execute(sql)
    conexao.commit()

def insert_cliente():
    nome = input('Nome do cliente: ')
    email = input('Email: ')
    telefone = input('Telefone (opcional): ')
    data_nascimento = input('Data de Nascimento (aaaa-mm-dd, opcional): ')
    sql = f"""INSERT INTO tb_clientes (nome, email, telefone, data_nascimento)
              VALUES ('{nome}', '{email}', '{telefone}', '{data_nascimento}')"""
    cursor.execute(sql)
    conexao.commit()

def select_produto():
    sql = 'SELECT * FROM tb_produto'
    cursor.execute(sql)
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)

def select_cliente():
    sql = 'SELECT * FROM tb_clientes'
    cursor.execute(sql)
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)

def delete_cliente():
    idt = int(input('ID do cliente a ser deletado: '))
    sql = f"DELETE FROM tb_clientes WHERE idt = {idt}"
    cursor.execute(sql)
    conexao.commit()

def main():
    create_database()
    global conexao, cursor
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table_produto()
    create_table_clientes()
    
    while True:
        print("\nMenu CRUD:")
        print("1. Inserir Produto")
        print("2. Inserir Cliente")
        print("3. Selecionar Produtos")
        print("4. Selecionar Clientes")
        print("5. Deletar Cliente")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            insert_produto()
        elif opcao == '2':
            insert_cliente()
        elif opcao == '3':
            select_produto()
        elif opcao == '4':
            select_cliente()
        elif opcao == '5':
            delete_cliente()
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

    close_connection(conexao, cursor)

if __name__ == '__main)__':
    main()
