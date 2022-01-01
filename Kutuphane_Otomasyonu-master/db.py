import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "",
    database = "kutuphane_otomasyon"
)

mycursor = mydb.cursor()


