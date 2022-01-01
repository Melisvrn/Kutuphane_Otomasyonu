import db
import uyeler_insert
import uyeler_update
from tkinter import messagebox

def query(name,surname,phone,mail,address):

    try:
        uyeler_insert.ekle(name,surname,phone,mail,address)
        print(db.mycursor.rowcount , " record inserted.")
        messagebox.showinfo("Uyarı","Kayıt edildi")
    except db.mysql.connector.errors.IntegrityError:
        print("user existing.")
        messagebox.showinfo("Uyarı","Böyle bir uye zaten var")

def giris(phone,mail):
    db.mycursor.execute("SELECT ID, uye_telefon, uye_eposta FROM kutuphane_otomasyonu.uye")
    rows = db.mycursor.fetchall()
    i = 0
    try:
        while i <= db.mycursor.rowcount :
            if(phone == str(rows[i][1])):
                if(mail == str(rows[i][2])):
                    print("GİRİS YAPİLDİ...",rows[i][0])
                    return rows[i][0]
            i += 1      
    except IndexError:
        print("Böyle bir uye yoktur.")
        return -1    


def queryUpdate(id,name,surname,phone,mail,adres):

    if(not(len(name) == 0 or len(surname) == 0 or len(phone) == 0 or len(mail) == 0 or len(adres) == 0 )):
        uyeler_update.fullUpdate(id,name,surname,phone,mail,adres) 

    else:
        messagebox.showerror("Uyarı","Bilgileriniz güncellenirken bir hata oluştu.") 
