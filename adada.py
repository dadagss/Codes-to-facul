import mysql.connector


conexao_db = mysql.connector.connect(user='root', password='', host='127.0.0.1')


print('Conexão:', conexao_db)
cursor_db = conexao_db.cursor()
sql = "CREATE DATABASE IF NOT EXISTS db_concessionaria"


cursor_db.execute(sql)
cursor_db.close()
conexao_db.close()

conexao_db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='db_concessionaria')
cursor_db = conexao_db.cursor()


sql = '''CREATE TABLE IF NOT EXISTS tb_veiculos (
        id_veiculo INT,
        Marca VARCHAR(255),
        Modelo VARCHAR(255),
        Ano DATE NOT NULL,
        Placa CHAR(20) NOT NULL,
        Preco DECIMAL(9,2) NOT NULL,
        PRIMARY KEY (id_veiculo)
    )'''

cursor_db.execute(sql)

sql = '''INSERT INTO tb_veiculos (id_veiculo, Marca, Modelo, Ano, Placa, Preco)
         VALUES (%s, %s, %s, %s, %s, %s)'''


dados_veiculos = [
    (1234568, 'Toyota', 'Corolla', '2022-01-01', 'ABC1234', 1500.25),
    (1234561, 'Honda', 'Civic', '2020-01-01', 'DEF5678', 1300.51),
    (1234563, 'Chevrolet', 'Onix', '2021-01-01', 'GHI9012', 1200.65),
    (1234564, 'Volkswagen', 'Golf', '2019-01-01', 'JKL3456', 1400.64),
    (1234562, 'Ford', 'Fiesta', '2018-01-01', 'MNO7890', 1100.14)
]


cursor_db.executemany(sql, dados_veiculos)


conexao_db.commit()
cursor_db.close()
conexao_db.close()
print('\nConexão fechada.')
