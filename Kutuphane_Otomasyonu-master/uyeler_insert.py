import db
import uyelikIslemleri as user

def ekle(name,surname,phone,mail,address):
 
    db.mycursor.execute('INSERT INTO kutuphane_otomasyonu.uye (`uye_ad`, `uye_soyad`, `uye_telefon`, `uye_eposta`, `uye_adres`) VALUES (%s, %s, %s, %s, %s)',
    (name,surname,phone,mail,address))
    db.mydb.commit()

