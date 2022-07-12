import mysql.connector
from mysqlx import DatabaseError

mydb = mysql.connector.connect(
  host="localhost",
  database="sucos_vendas",
  port= "3306",
  user="root",
  password="49650812"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT NUMERO, CODIGO_DO_PRODUTO FROM  itens_notas_fiscais;")

myresult = mycursor.fetchall()

#print(myresult)#

