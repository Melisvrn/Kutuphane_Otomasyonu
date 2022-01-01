from tkinter import *
import uyeler_insert
import uyeler_query
import uyeGirisi

def uyelikIslemleriEkrani():
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
    
    Label(yeniPencere, text = "Telefon Numarası",bg="#1C2833", fg="yellow", font="Times 12 italic").place(x=50, y=110)
    telNoTextbox = Entry(yeniPencere,font="Times 12 bold")
    telNoTextbox.place(x=170, y=110)

    Label(yeniPencere, text = "Mail Adresi",bg="#1C2833", fg="yellow", font="Times 12 italic").place(x=50, y=150)
    mailTextbox = Entry(yeniPencere,font="Times 12 bold")
    mailTextbox.place(x=170, y=150)

    girisYapButton = Button(yeniPencere, text = "Giriş",font="Times 12 bold" ,command = lambda:uyeGirisi.uyeGirisEkrani(telNoTextbox.get(),mailTextbox.get()))
    girisYapButton.place(x=260, y=200)
    
    kayitEkranButton = Button(yeniPencere, text = "Kayıt Ol",font="Times 12 bold" ,command = kayıtOlmaEkrani)
    kayitEkranButton.place(x=241, y=270)

def kayıtOlmaEkrani():
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

    Label(yeniPencere, text = "Ad",bg="#1C2833", fg="yellow", font="Times 11 italic").grid(padx = 35, pady = 15, sticky = W)
    adTextbox = Entry(yeniPencere,font="Times 12")
    adTextbox.grid(row = 0, column = 1, sticky = E)
    
    Label(yeniPencere, text = "Soyad",bg="#1C2833", fg="yellow", font="Times 11 italic").grid(padx = 35, pady = 15, sticky = W)
    soyadTextbox = Entry(yeniPencere,font="Times 12")
    soyadTextbox.grid(row = 1, column = 1, sticky = E)

    Label(yeniPencere, text = "Telefon Numarası",bg="#1C2833", fg="yellow", font="Times 11 italic").grid(padx = 35, pady = 15, sticky = W)
    telNoTextbox = Entry(yeniPencere,font="Times 12")
    telNoTextbox.grid(row = 2, column = 1, sticky = E)

    Label(yeniPencere, text = "Mail",bg="#1C2833", fg="yellow", font="Times 11 italic").grid(padx = 35, pady = 15, sticky = W)
    mailTextbox = Entry(yeniPencere,font="Times 12")
    mailTextbox.grid(row = 3, column = 1, sticky = E)

    Label(yeniPencere, text = "Adres",bg="#1C2833", fg="yellow", font="Times 11 italic").grid(padx = 35, pady = 15, sticky = W)
    adresTextbox = Entry(yeniPencere,font="Times 12")
    adresTextbox.grid(row = 4, column = 1, sticky = E)

    kayitYapButton = Button(yeniPencere, text = "Kayıt Ol",font="Times 12 bold", 
    command = lambda : uyeler_query.query(adTextbox.get(),soyadTextbox.get(),telNoTextbox.get(),mailTextbox.get(),adresTextbox.get()))
    kayitYapButton.grid(row = 6, column = 1, sticky = E)
