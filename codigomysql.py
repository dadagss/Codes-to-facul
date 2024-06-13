import mysql.connector
import os
import time
import pyfiglet

def create_database():
    conexao_db = mysql.connector.connect(user='root',password='',host='127.0.0.1')
    print('Conexão DB', conexao_db)
    sql = "CREATE DATABASE if not exists db_cadastro"
    cursor = conexao_db.cursor()
    cursor.execute(sql)
    cursor.close()
    conexao_db.close()

def create_con():
    con = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='db_cadastro')
    return con

def close_con():
    cursor.close()
    conexao.close()
    print('Conexão fechada')

def create_table():
    
    #TABELA CARGO

    sql = '''CREATE TABLE if not exists tb_cargo(
                idt int NOT NULL AUTO_INCREMENT,
                nome varchar(45) NOT NULL,
                PRIMARY KEY (idt)
        )
        '''
    
    #TABELA EMPREGADO

    cursor.execute(sql)
    sql = '''CREATE TABLE if not exists tb_empregado(
                idt int NOT NULL AUTO_INCREMENT,
                nome varchar(45) NOT NULL,
                dta_nascimento date NULL,
                genero enum('M','F') NOT NULL,
                cod_cargo int NOT NULL,
                PRIMARY KEY (idt),
                FOREIGN KEY (cod_cargo) REFERENCES td_cargo(idt)
    )'''
    cursor.execute(sql)

def insert_cargo():
    a_nome = input('Nome do cargo: ')
    sql = f''' insert into tb_cargo (nome)
                values('{a_nome}')'''
    cursor.execute(sql)
    conexao.commit()

def insert_empregado():
    a_nome = input("Digite seu nome: ")
    a_dta = input("Digite a data de nascimento (yyyy-mm-dd): ")
    while True:
        gen = input("Digite 1 se for mulher, digite 2 se for homem: ")
        if gen == '1':
            gen = 'F'
            break
        elif gen == '2':
            gen = 'M'
            break
        else:
            print('Opção inválida')
            continue
    try:
        cod_cargo = int(input("Digite o id do cargo do empregado: "))
    except ValueError: 
        print('Digite um valor válido')
        return

    sql = f"insert into tb_empregado (nome, dta_nascimento, genero, cod_cargo) values ('{a_nome}', '{a_dta}', '{gen}', {cod_cargo})"
    
    cursor.execute(sql)
    conexao.commit()
    print("Aplicação bem sucedida")


def select_cargo():
    sql = "SELECT * FROM tb_cargo"
    cursor.execute(sql)
    registros = cursor.fetchall()
    for x in registros:
        print(x)
    print('Registros na horizontal')
    print(registros)
    print('Registros bonitinhos')
    for registro in registros:
        print("- idt: ", registro[0])
        print("nome: ", registro[1])

def select_funcionario():
    sql = "SELECT * FROM tb_empregado"
    cursor.execute(sql)
    print('Registros na Vertical')
    registros = cursor.fetchall()
    for x in registros:
        print(x)
    print('Registros na horizontal')
    print(registros)
    for registro in registros:
        print("- idt: ", registro[0])
        print("nome: ", registro[1])
        print("Data de nascimento: ", registro[2])
        print("Gênero: ", registro[3])
        print("Codigo do cargo ", registro[4])
        
def delete_cargo():
    try:
        cod = int(input("Digite o id do cargo que você deseja deletar: "))
    except ValueError:
        print("Por favor, digite um ID válido.")
        return
    
    try:
        sql = "DELETE FROM tb_cargo WHERE idt = %s"
        cursor.execute(sql, (cod,))
        conexao.commit()
        print(f"Cargo com ID {cod} deletado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao deletar o cargo: {str(e)}")


def delete_empregado():
    try:
        cod = int(input("Digite o id do cargo que você deseja deletar: "))
        sql = f"DELETE FROM tb_empregado WHERE idt = {cod}"
        cursor.execute(sql)
        conexao.commit()        
        print(f"Cargo do id {cod} deletado")
    except ValueError:
        print("Digite um valor valido")


def main():

    apoint = None
    while True:
        print('''🔥🦖 - MENU - 💣🐉
                1 - insert cargo
                2 - insert empregado
                3 - delete cargo
                4 - delete empregado
                5 - vizualiza os cargos
                6 - vizualiza funcionarios
                0 - close connection
              ''')
        
        try:
            apoint = int(input("Digite a opção Desejada: "))
            if apoint == 1:
                insert_cargo()
                time.sleep(3)
                os.system('cls')
            elif apoint == 2:
                insert_empregado()
                time.sleep(3)
                os.system('cls')
            elif apoint == 3:
                delete_cargo()
                time.sleep(3)
                os.system('cls')
            elif apoint == 4:
                delete_empregado()
                time.sleep(3)
                os.system('cls')
            elif apoint == 5:
                select_cargo()
                # time.sleep(5)
                # os.system('cls')
            elif apoint == 6:
                select_funcionario()
                # time.sleep(5)
                # os.system('cls')
            elif apoint == 0:
                close_con
                print("Saindo...")
                time.sleep(5)
                return False
            else:
                print("Digite o numero de 1 a 6")
                continue

        except ValueError:
            texto = "ESCREVA UM NUMERO!!"
            ascii_art = pyfiglet.figlet_format(texto)
            print(ascii_art)
            time.sleep(5)
            continue        


        


if __name__ == '__main__':
    create_database()
    conexao = create_con()
    cursor = conexao.cursor()
    main()
