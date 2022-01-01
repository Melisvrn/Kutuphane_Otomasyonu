from tkinter import *
from tkinter.font import BOLD
import uyeler_query
import uyeler_listele

def getUser(id,ad,soyad,tel,mail,adres):
    user = uyeler_listele.onlyOneUser(id)
    ad.set(user[0][1])
    soyad.set(user[0][2])
    tel.set(user[0][3])
    mail.set(user[0][4])
    adres.set(user[0][5])

def uyeBilgiGuncelle(id):

    yeniPencere = Toplevel()
    yeniPencere.title("Bilgi Güncelleme")
    yeniPencere.geometry("820x700")
    yeniPencere['background'] = '#1C2833'
    
    pgen = 820
    pyuks = 700

    ekrangen = yeniPencere.winfo_screenwidth()
    ekranyuks = yeniPencere.winfo_screenheight()

    x = (ekrangen - pgen) / 2
    y = (ekranyuks - pyuks) / 2

    yeniPencere.geometry("%dx%d+%d+%d"%(pgen, pyuks, x, y))

    ad= StringVar()
    soyad= StringVar()
    tel= StringVar()
    mail= StringVar()
    adres= StringVar()

    Label(yeniPencere,text="Kullanıcı Bilgileri",font='arial 20 bold',fg="white",bg="#99004d").pack(padx=35,pady=15)

    frame = Frame(yeniPencere,bg="#1C2833")
    frame.pack(padx=5,pady=50)

    Label(frame, text = "Ad",font='arial 12',fg="white",bg="#1C2833").grid(row=0,column=0,padx = 25, pady = 15, sticky = W)
    adTextbox = Entry(frame, textvariable= ad,width=30,font=('Arial',12))
    adTextbox.grid(row = 0, column = 1, sticky = E)
    
    Label(frame, text = "Soyad",font='arial 12',fg="white",bg="#1C2833").grid(padx = 25, pady = 15, sticky = W)
    soyadTextbox = Entry(frame , textvariable =soyad,width=30,font=('Arial',12))
    soyadTextbox.grid(row = 1, column = 1, sticky = E)

    Label(frame, text = "Telefon Numarası",font='arial 12',fg="white",bg="#1C2833").grid(padx = 25, pady = 15, sticky = W)
    telNoTextbox = Entry(frame, textvariable=tel,width=30,font=('Arial',12))
    telNoTextbox.grid(row = 2, column = 1, sticky = E)

    Label(frame, text = "Mail",font='arial 12',fg="white",bg="#1C2833").grid(padx = 25, pady = 15, sticky = W)
    mailTextbox = Entry(frame,textvariable=mail,width=30,font=('Arial',12))
    mailTextbox.grid(row = 3, column = 1, sticky = E) 

    Label(frame,text="Adres :",font='arial 12',fg="white",bg="#1C2833").grid(row=4,column=0,padx = 25, pady = 15, sticky = W)
    adresTextbox = Entry(frame,textvariable=adres,width=30,font=('Arial',12))
    adresTextbox.grid(row = 4, column = 1, sticky = E)
    

    getUser(id,ad,soyad,tel,mail,adres)

    kayitYapButton = Button(yeniPencere, text = "Güncelle", 
    command = lambda : uyeler_query.queryUpdate(id,adTextbox.get(),soyadTextbox.get(),mailTextbox.get(),telNoTextbox.get(),adresTextbox.get()),
    bg='#99004d', fg='White',font='arial 11',height=3, width=10,relief="groove")
    kayitYapButton.pack()
