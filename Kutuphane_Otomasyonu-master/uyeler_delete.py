import db

def delete():
    db.mycursor.execute('DELETE FROM kutuphane_otomasyonu.uye WHERE id_uye = %s',
    (400,))
    db.mydb.commit()


    print(db.mycursor.rowcount , " kullanıcı silindi.")

    db.mycursor.close()
    db.mydb.close()


