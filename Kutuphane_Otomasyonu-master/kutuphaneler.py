from tkinter import *
import db
import kutuphaneKitapligi

# def kutuphane():
#     db.mycursor.execute("SELECT kütüphane_isim FROM kutuphane_otomasyonu.kütüphaneler")
#     rows = db.mycursor.fetchall()
#     return rows

def kutuphaneSecim(uyeID):
    yeniPencere = Toplevel()
    yeniPencere.title("Kütüphaneler")
    yeniPencere.geometry("350x370")
    yeniPencere['background'] = '#1C2833'

    pgen = 400
    pyuks = 370

    ekrangen = yeniPencere.winfo_screenwidth()
    ekranyuks = yeniPencere.winfo_screenheight()

    x = (ekrangen - pgen) / 2
    y = (ekranyuks - pyuks) / 2

    yeniPencere.geometry("%dx%d+%d+%d"%(pgen, pyuks, x, y))

    kutuphaneA_Button = Button(yeniPencere, text = "Bursa Şehir Kütüphanesi\nYıldırım/Bursa", width = 24, height = 3,bg="#009999",fg="white",command = lambda : kutuphaneKitapligi.kitapDoldur("Bursa Şehir Kütüphanesi", uyeID))
    kutuphaneA_Button.grid(padx = 108, pady = 50)
    kutuphaneB_Button = Button(yeniPencere, text = "Bursa Araştırma Kütüphanesi\nOsmangazi/Bursa", width = 24, height = 3,bg="#99004d",fg="white", command = lambda : kutuphaneKitapligi.kitapDoldur("Bursa Araştırma Kütüphanesi", uyeID))
    kutuphaneB_Button.grid(padx = 108, pady = 2)
    kutuphaneC_Button = Button(yeniPencere, text = "Akkılıç Kütüphanesi\nNilüfer/Bursa", width = 24, height = 3,bg="#ff9900",fg="white", command = lambda : kutuphaneKitapligi.kitapDoldur("Akkılıç Kütüphanesi", uyeID))
    kutuphaneC_Button.grid(padx = 108, pady = 50)
