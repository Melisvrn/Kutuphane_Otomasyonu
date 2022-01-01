import db

def emaneAlinanKitaplar(uye_id):
    db.mycursor.execute(
        "SELECT kitap_ISBN, kitaplar.kitap_ismi, concat(uye.uye_ad,' ',uye.uye_soyad) AS uye,\
        kütüphaneler.kütüphane_isim,alım_tarihi, teslim_tarihi FROM (((kutuphane_otomasyonu.emanet \
        INNER JOIN kutuphane_otomasyonu.kitaplar ON emanet.kitap_ISBN = kitaplar.ISBN_no_kitap)\
        INNER JOIN kutuphane_otomasyonu.kütüphaneler ON emanet.kutuphane_ID = kütüphaneler.id)\
        INNER JOIN kutuphane_otomasyonu.uye ON emanet.uye_ID = uye.ID) WHERE uye_ID = %s AND emanet_durumu = 0",(uye_id,))
    rows = db.mycursor.fetchall()
    print(rows)
    return rows

def emaneAlinanKitaplarSayısı(uye_id):
    db.mycursor.execute(
        "SELECT kitap_ISBN, kitaplar.kitap_ismi, concat(uye.uye_ad,' ',uye.uye_soyad) AS uye,\
        kütüphaneler.kütüphane_isim,alım_tarihi, teslim_tarihi FROM (((kutuphane_otomasyonu.emanet \
        INNER JOIN kutuphane_otomasyonu.kitaplar ON emanet.kitap_ISBN = kitaplar.ISBN_no_kitap)\
        INNER JOIN kutuphane_otomasyonu.kütüphaneler ON emanet.kutuphane_ID = kütüphaneler.id)\
        INNER JOIN kutuphane_otomasyonu.uye ON emanet.uye_ID = uye.ID) WHERE uye_ID = %s AND emanet_durumu = 0",(uye_id,))
    rows = db.mycursor.fetchall()
    count_row = db.mycursor.rowcount
    return count_row


def teslimEdilenKitaplar(uye_id):
    db.mycursor.execute(
        "SELECT kitap_ISBN, kitaplar.kitap_ismi, concat(uye.uye_ad,' ',uye.uye_soyad) AS uye,\
        kütüphaneler.kütüphane_isim,alım_tarihi, teslim_tarihi FROM (((kutuphane_otomasyonu.emanet \
        INNER JOIN kutuphane_otomasyonu.kitaplar ON emanet.kitap_ISBN = kitaplar.ISBN_no_kitap)\
        INNER JOIN kutuphane_otomasyonu.kütüphaneler ON emanet.kutuphane_ID = kütüphaneler.id)\
        INNER JOIN kutuphane_otomasyonu.uye ON emanet.uye_ID = uye.ID) WHERE uye_ID = %s AND emanet_durumu = 1",(uye_id,))
    rows = db.mycursor.fetchall()
    print(rows)
    return rows

def teslimEdilenKitaplarSayısı(uye_id):
    db.mycursor.execute(
        "SELECT kitap_ISBN, kitaplar.kitap_ismi, concat(uye.uye_ad,' ',uye.uye_soyad) AS uye,\
        kütüphaneler.kütüphane_isim,alım_tarihi, teslim_tarihi FROM (((kutuphane_otomasyonu.emanet \
        INNER JOIN kutuphane_otomasyonu.kitaplar ON emanet.kitap_ISBN = kitaplar.ISBN_no_kitap)\
        INNER JOIN kutuphane_otomasyonu.kütüphaneler ON emanet.kutuphane_ID = kütüphaneler.id)\
        INNER JOIN kutuphane_otomasyonu.uye ON emanet.uye_ID = uye.ID) WHERE uye_ID = %s AND emanet_durumu = 1",(uye_id,))
    rows = db.mycursor.fetchall()
    count_row = db.mycursor.rowcount
    return count_row

def teslimEt(emanetNo):
    db.mycursor.execute("UPDATE kutuphane_otomasyonu.emanet SET emanet_durumu = 1 WHERE id= %s",(emanetNo,))
    db.mydb.commit()
