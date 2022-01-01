import db

def update(val1,id):
    update = db.mycursor.execute('UPDATE kutuphane_otomasyonu.uye SET uye_eposta = %s WHERE ID = %s',
    (val1,id))
    db.mydb.commit()

    print(str(update) + " kullanıcı güncellendi.")

    db.mycursor.close()
    db.mydb.close()

def fullUpdate(id,name,surname,phone,mail,address):
    update = db.mycursor.execute('UPDATE kutuphane_otomasyonu.uye SET uye_ad = %s , uye_soyad = %s ,uye_telefon = %s ,uye_eposta = %s ,uye_adres = %s WHERE ID = %s',
    (name,surname,mail,phone,address,id))
    db.mydb.commit()
    print(str(update) + " kullanıcı güncellendi.")

"""
id_uye
uye_ad
uye_soyad
uye_telefon
uye_eposta
uye_adres
"""




