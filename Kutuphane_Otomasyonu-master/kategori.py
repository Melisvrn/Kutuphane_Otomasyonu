import db

def kategoriListele():
    db.mycursor.execute("SELECT * FROM kutuphane_otomasyonu.kategoriler")
    rows = db.mycursor.fetchall()
    print(rows)
    return rows


def selectByCategory(item):
    
    db.mycursor.execute("SELECT kitaplar.ISBN_no_kitap, kitaplar.kitap_ismi,concat(yazarlar.yazar_ad,' ',yazarlar.yazar_soyad) AS yazar,\
        kitaplar.kitap_yayınevi, kitaplar.basim_yili, kategoriler.tur,\
        kitaplar.kitap_sayisi  FROM ((((kutuphane_otomasyonu.kitaplar \
        INNER JOIN kutuphane_otomasyonu.kitap_kategori ON kitaplar.ISBN_no_kitap = kitap_kategori.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.kategoriler ON kitap_kategori.id_kategori = kategoriler.id)\
        INNER JOIN kutuphane_otomasyonu.kitap_yazar ON kitaplar.ISBN_no_kitap = kitap_yazar.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.yazarlar ON kitap_yazar.id_yazar = yazarlar.id ) WHERE tur = %s",(item,))
    rows = db.mycursor.fetchall()
    print(rows)
    return rows

              
