import db

def kitaplistele():
    db.mycursor.execute("SELECT kitaplar.ISBN_no_kitap, kitaplar.kitap_ismi, concat(yazarlar.yazar_ad,' ',yazarlar.yazar_soyad) AS yazar,\
        kitaplar.kitap_yayınevi, kitaplar.basim_yili, kategoriler.tur,\
        kitaplar.kitap_sayisi  FROM ((((kutuphane_otomasyonu.kitaplar \
        INNER JOIN kutuphane_otomasyonu.kitap_kategori ON kitaplar.ISBN_no_kitap = kitap_kategori.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.kategoriler ON kitap_kategori.id_kategori = kategoriler.id)\
        INNER JOIN kutuphane_otomasyonu.kitap_yazar ON kitaplar.ISBN_no_kitap = kitap_yazar.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.yazarlar ON kitap_yazar.id_yazar = yazarlar.id)")
    rows = db.mycursor.fetchall()
    print(rows)
    return rows


def kitaplistele2(id):
    db.mycursor.execute("SELECT kitaplar.ISBN_no_kitap, kitaplar.kitap_ismi, concat(yazarlar.yazar_ad,' ',yazarlar.yazar_soyad) AS yazar,\
        kitaplar.kitap_yayınevi, kitaplar.basim_yili, kategoriler.tur,\
        kitaplar.kitap_sayisi FROM (((((kutuphane_otomasyonu.kitap_kütüphane\
        INNER JOIN kitaplar ON kitap_kütüphane.ISBN_kitap= kitaplar.ISBN_no_kitap)\
        INNER JOIN kutuphane_otomasyonu.kitap_kategori ON kitaplar.ISBN_no_kitap = kitap_kategori.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.kategoriler ON kitap_kategori.id_kategori = kategoriler.id)\
        INNER JOIN kutuphane_otomasyonu.kitap_yazar ON kitaplar.ISBN_no_kitap = kitap_yazar.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.yazarlar ON kitap_yazar.id_yazar = yazarlar.id) WHERE kitap_kütüphane.id_kütüphane = %s",(id,))
    rows = db.mycursor.fetchall()
    print(rows)
    return rows

kitaplistele2(2)

def searchByName(item):
    db.mycursor.execute("SELECT kitaplar.ISBN_no_kitap, kitaplar.kitap_ismi,concat(yazarlar.yazar_ad,' ',yazarlar.yazar_soyad) AS yazar,\
        kitaplar.kitap_yayınevi, kitaplar.basim_yili, kategoriler.tur,\
        kitaplar.kitap_sayisi  FROM ((((kutuphane_otomasyonu.kitaplar \
        INNER JOIN kutuphane_otomasyonu.kitap_kategori ON kitaplar.ISBN_no_kitap = kitap_kategori.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.kategoriler ON kitap_kategori.id_kategori = kategoriler.id)\
        INNER JOIN kutuphane_otomasyonu.kitap_yazar ON kitaplar.ISBN_no_kitap = kitap_yazar.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.yazarlar ON kitap_yazar.id_yazar = yazarlar.id ) WHERE kitap_ismi = %s",(item,))
    rows = db.mycursor.fetchall()
    print(rows)
    return rows



def searchByISBN(item):
    db.mycursor.execute("SELECT kitaplar.ISBN_no_kitap, kitaplar.kitap_ismi,concat(yazarlar.yazar_ad,' ',yazarlar.yazar_soyad) AS yazar,\
        kitaplar.kitap_yayınevi, kitaplar.basim_yili, kategoriler.tur,\
        kitaplar.kitap_sayisi  FROM ((((kutuphane_otomasyonu.kitaplar \
        INNER JOIN kutuphane_otomasyonu.kitap_kategori ON kitaplar.ISBN_no_kitap = kitap_kategori.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.kategoriler ON kitap_kategori.id_kategori = kategoriler.id)\
        INNER JOIN kutuphane_otomasyonu.kitap_yazar ON kitaplar.ISBN_no_kitap = kitap_yazar.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.yazarlar ON kitap_yazar.id_yazar = yazarlar.id ) WHERE ISBN_no_kitap = %s",(item,))
    rows = db.mycursor.fetchall()
    print(rows)
    return rows


def searchByAuthor(item):
    db.mycursor.execute("SELECT kitaplar.ISBN_no_kitap, kitaplar.kitap_ismi,concat(yazarlar.yazar_ad,' ',yazarlar.yazar_soyad) AS yazar,\
        kitaplar.kitap_yayınevi, kitaplar.basim_yili, kategoriler.tur,\
        kitaplar.kitap_sayisi  FROM ((((kutuphane_otomasyonu.kitaplar \
        INNER JOIN kutuphane_otomasyonu.kitap_kategori ON kitaplar.ISBN_no_kitap = kitap_kategori.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.kategoriler ON kitap_kategori.id_kategori = kategoriler.id)\
        INNER JOIN kutuphane_otomasyonu.kitap_yazar ON kitaplar.ISBN_no_kitap = kitap_yazar.ISBN_kitap)\
        INNER JOIN kutuphane_otomasyonu.yazarlar ON kitap_yazar.id_yazar = yazarlar.id ) WHERE yazar_ad = %s",(item,))

    rows = db.mycursor.fetchall()
    print(rows)
    return rows
