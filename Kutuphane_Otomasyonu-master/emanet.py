import db
import kutuphaneKitapligi
import kitap_emanet_teslim
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
from datetime import date, datetime, timedelta


today = date.today()
nexttime = datetime.now() + timedelta(days=14)

def stok(kitap_ISBN):
    db.mycursor.execute('SELECT kitap_sayisi FROM kutuphane_otomasyonu.kitaplar WHERE ISBN_no_kitap = %s',(kitap_ISBN,))
    result = db.mycursor.fetchall()
    return result[0][0]

def stokGuncelle(kitap_ISBN):
    result = stok(kitap_ISBN)
    db.mycursor.execute('UPDATE kutuphane_otomasyonu.kitaplar SET kitap_sayisi = %s WHERE ISBN_no_kitap = %s',(result-1, kitap_ISBN))
    db.mydb.commit()

def kitabiAl(uyeID, kitap_ISBN, kutuphane_id):
    db.mycursor.execute("INSERT INTO kutuphane_otomasyonu.emanet (`uye_ID`, `kitap_ISBN`, `kutuphane_ID`, `alım_tarihi`, `teslim_tarihi`, `emanet_durumu`) VALUES (%s, %s, %s, %s, %s, %s)",
    (uyeID, kitap_ISBN, kutuphane_id, today.strftime("%Y-%m-%d"), nexttime, 0))

    db.mydb.commit()
    stokGuncelle(kitap_ISBN)

def emanetAl(uyeID, kitap_ISBN, kutuphane_id, pencere, secim):
    if (stok(kitap_ISBN) > 0):
        kitabiAl(uyeID, kitap_ISBN, kutuphane_id)
        pencere.destroy()
        kutuphaneKitapligi.kitapDoldur(secim, uyeID)
    else:
        messagebox.showerror("Kitap Yok", "Alacak olduğunuz kitap şuan stokta bulunmamaktadır.")

def emanetTeslim(uyeID):

    def alinanKitaplar(uyeID):
        db.mycursor.execute('SELECT uye_ID, kitap_ISBN, kutuphane_ID, alım_tarihi, teslim_tarihi, emanet_durumu FROM kutuphane_otomasyonu.emanet WHERE uye_ID = %s',(uyeID,))
        rows = db.mycursor.fetchall()
        print(rows)
        return rows
    
    yeniPencere = Toplevel()
    yeniPencere.title("İşlemlerim")
    yeniPencere.geometry("820x700")
   
    pgen = 820
    pyuks = 700

    ekrangen = yeniPencere.winfo_screenwidth()
    ekranyuks = yeniPencere.winfo_screenheight()

    x = (ekrangen - pgen) / 2
    y = (ekranyuks - pyuks) / 2

    yeniPencere.geometry("%dx%d+%d+%d"%(pgen, pyuks, x, y))

    wrapper2 = LabelFrame(yeniPencere,text="KİTAPLAR",height=120)
    wrapper2.pack(fill="both",expand="yes",padx=20,pady=8)

    kitapListeleTree = Treeview(wrapper2,column=("1","2","3","4","5","6"), 
                            show='headings',height="4",
                            selectmode="extended")
    kitapListeleTree.pack(side="left")
    kitapListeleTree.place(x=0,y=0)

    #vertical scrollbar
    yscroolbar = Scrollbar(wrapper2, orient= "vertical",
                            command=kitapListeleTree.yview)
    yscroolbar.pack(side='right',fill=Y)
    #horizantal scrollbar
    xscroolbar = Scrollbar(wrapper2,orient="horizontal",
                            command=kitapListeleTree.xview)
    xscroolbar.pack(side=BOTTOM,fill=X)

    kitapListeleTree.config(yscrollcommand=yscroolbar.set, 
                            xscrollcommand=xscroolbar.set)

    kitapListeleTree.column("#1",anchor = CENTER,width=120,minwidth = 130)
    kitapListeleTree.heading("#1",text="ISBN")

    kitapListeleTree.column("#2",anchor = CENTER,width=160,minwidth = 170)
    kitapListeleTree.heading("#2",text="Kitap")

    kitapListeleTree.column("#3",anchor = CENTER,width=150,minwidth = 160)
    kitapListeleTree.heading("#3",text="Kütüphane")

    kitapListeleTree.column("#4",anchor = CENTER,width=100,minwidth = 100)
    kitapListeleTree.heading("#4",text="Alım Tarihi")

    kitapListeleTree.column("#5",anchor = CENTER,width=100,minwidth = 110)
    kitapListeleTree.heading("#5",text="Teslim Tarihi")

    kitapListeleTree.column("#6",anchor = CENTER,width=100,minwidth = 110)
    kitapListeleTree.heading("#6",text="Durumu")

    kitaplar = kitap_emanet_teslim.emaneAlinanKitaplar(uyeID)
    
    for i in range(len(kitaplar)):
        kitapListeleTree.insert('', 'end', values = kitaplar[i])

    #btn1 = Button(yeniPencere,text="Ara",command = lambda : alinanKitaplar(uyeID),
    #            bg= 'blue',fg='white',width=5)
    #btn1.grid(row=0,column=0,padx=5,pady=3)
