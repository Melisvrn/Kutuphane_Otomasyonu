import db

def listele():
    db.mycursor.execute("SELECT * FROM kutuphane_otomasyonu.uye")
    rows = db.mycursor.fetchall()
    print("Read",db.mycursor.rowcount,"row(s) of data.")

    for row in rows:
        print("Data row = (%s, %s, %s, %s, %s, %s,%s)" %(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))


    db.mycursor.close()
    db.mydb.close()

def onlyOneUser(id):
    db.mycursor.execute("SELECT * FROM kutuphane_otomasyonu.uye WHERE ID = %s",(id,))
    row= db.mycursor.fetchall()

    print("Read",db.mycursor.rowcount,"row(s) of data.")
    print(row)
   
    return row  
