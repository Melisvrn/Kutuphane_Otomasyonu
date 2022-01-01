import db

db.mycursor.execute("CREATE TABLE üyeler (id_uye INT PRIMARY KEY, uye_adı VARCHAR(45), uye_soyad VARCHAR(45), uye_tel VARCHAR(45), uye_eposta VARCHAR(45), uye_adres VARCHAR(45) )" )
db.mydb.commit()


print("Finished creating table.")


db.mycursor.close()
db.mydb.close()








