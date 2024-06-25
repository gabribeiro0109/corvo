rom datetime import datetime
from selenium import webdriver
import psycopg2
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
url = 'https://www.google.com/finance/quote/USD-BRL?sa=X&sqi=
2&ved=2ahUKEwjHod2jweyEAxV4LrkGHTzSCNsQmY0JegQIDhAv'
driver.get(url)
dolar_element = driver.find_element('xpath', "/html/body/c-wi
z[2]/div/div[4]/div/main/div[2]/div[1]/c-wiz/div/div[1]/div/d
Desafio Pipeline, rodar arquivo de RPA Dolar: 2
iv[1]/div/div[1]/div/span/div/div")
dolar = float(dolar_element.text.replace(',', '.'))
data_hora_atual = datetime.now()
data_formatada = data_hora_atual.strftime("%m/%d/%Y")
hora_formatada = data_hora_atual.strftime("%H:%M")
print(f'Na data {data_formatada} e no horário {hora_formatad
a} um dólar está cotado em R${dolar}')
dados = {'cotacao': [dolar], 'data': [data_formatada], 'hor
a': [hora_formatada]}
host = 'pg-124c7786-davicavalcante3298-d32e.g.aivencloud.com'
database = 'defaultdb'
user = 'avnadmin'
password = 'AVNS_AFI1hpLtTqpP_3CTdbC'
port = '18234'
try:
 connection = psycopg2.connect(host=host, database=databas
e, user=user, password=password, port=port)
 cursor = connection.cursor()
 # sql_create_table = """
 # CREATE TABLE cotacao_dolar (
 # id SERIAL PRIMARY KEY,
 # data DATE,
 # hora TIME,
 # cotacao DECIMAL(10,2)
 # );
 # """
 
 # cursor.execute(sql_create_table)
 
Desafio Pipeline, rodar arquivo de RPA Dolar: 3
 # sql_create_procedure = """
 # CREATE OR REPLACE PROCEDURE inserir_cotacao_dolar(
 # data_in DATE,
 # hora_in TIME,
 # cotacao_in DECIMAL(10,2)
 # )
 # LANGUAGE SQL
 # AS $$
 # INSERT INTO cotacao_dolar (data, hora, cotacao)
 # VALUES (data_in, hora_in, cotacao_in);
 # $$;
 # """
 
 # cursor.execute(sql_create_procedure)
 
 cursor.execute("CALL inserir_cotacao_dolar(%s, %s, %s);",
(data_formatada, hora_formatada, dolar))
 
 connection.commit()
 
 cursor.execute("SELECT * FROM cotacao_dolar;")
 records = cursor.fetchall()
 for row in records:
 print(row)
 cursor.close()
 connection.close()
except (Exception, psycopg2.Error) as error:
 print("Erro ao conectar ao PostgreSQL:", error)
