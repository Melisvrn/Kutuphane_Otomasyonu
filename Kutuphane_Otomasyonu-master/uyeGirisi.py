from tkinter import *
import kutuphaneler
import uyeler_query
import uyeBilgiGüncelleme
import emanet
import kitapIslemleri

def uyeGirisEkrani(telNo, eMail):
    ID = uyeler_query.giris(telNo, eMail)
    if  ID > -1:
        yeniPencere = Toplevel()
        yeniPencere.title("Üyelik İşlemleri")
        yeniPencere.geometry("350x370")
        yeniPencere['background'] = '#1C2833'

        pgen = 400
        pyuks = 370

        ekrangen = yeniPencere.winfo_screenwidth()
        ekranyuks = yeniPencere.winfo_screenheight()

        x = (ekrangen - pgen) / 2
        y = (ekranyuks - pyuks) / 2

        yeniPencere.geometry("%dx%d+%d+%d"%(pgen, pyuks, x, y))
        
        kutuphaneButton = Button(yeniPencere, text = "Kütüphaneler",width = 17, height = 3, 
                                command = lambda : kutuphaneler.kutuphaneSecim(ID),
                                 bg="#cc3300",fg="white")
        kutuphaneButton.grid(row = 0, column = 0, padx = 50, pady = 50)
        islemlerimButton = Button(yeniPencere, text = "İşlemlerim", width = 17, height = 3, 
                                command = lambda : emanet.emanetTeslim(ID),
                                bg="#009999",fg="white")
        islemlerimButton.grid(row = 0, column = 1, padx = 10, pady = 50)
        ayarlarButton = Button(yeniPencere, text = "Ayarlar", width = 17, height = 3, 
                            command = lambda : uyeBilgiGüncelleme.uyeBilgiGuncelle(ID),
                            bg="#99004d",fg="white")
        ayarlarButton.grid(row = 1, column = 0, padx = 50, pady = 50)
        kitaplarım = Button(yeniPencere, text="Kitaplarım",width=17, height = 3, 
                            command = lambda : kitapIslemleri.kitapGecmisi(ID),
                           bg="#ff9900",fg="white")
        kitaplarım.grid(row = 1, column = 1, padx = 10, pady = 50)