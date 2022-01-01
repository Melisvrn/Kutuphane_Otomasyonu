from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import db
import kitaplar_listele
import kategori
import emanet

def kitapDoldur(secim, uyeID):
    
    def kutuphane():
        db.mycursor.execute("SELECT kütüphane_isim FROM kutuphane_otomasyonu.kütüphaneler")
        rows = db.mycursor.fetchall()
        return rows

    def kutuphaneIDBelirle():
        kutuphaneler = kutuphane()

        for i in range(len(kutuphaneler)):
            if secim == kutuphaneler[i][0]:
                return i+1

    kutuphaneID = kutuphaneIDBelirle()

    def update(rows):
        kitapListeleTree.delete(*kitapListeleTree.get_children())
        for i in rows:
            kitapListeleTree.insert("",END,values = i)

    def getrow(event):
        rowid = kitapListeleTree.identify_row(event.y)
        item = kitapListeleTree.item(kitapListeleTree.focus())
        s1.set(item['values'][0]) 
        s2.set(item['values'][1])
        s3.set(item['values'][2])
        s4.set(item['values'][3])
        s5.set(item['values'][4])
        s6.set(item['values'][5]) 

    def items_selected(event):
        selected_indices = kategoriListeleListbox.curselection() #0,1,2,3,4,5,6,7,8,
        kitap_ktg = kategori.selectByCategory(kategoriListeleListbox.get(selected_indices))
        update(kitap_ktg)
       
    def adaGoreBul():
        kitap_adı = t1.get()
        kitaplar = kitaplar_listele.searchByName(kitap_adı)
        update(kitaplar)

    def ısbnGoreBul():
        kitap_ısbn = t2.get()
        kitaplar = kitaplar_listele.searchByISBN(kitap_ısbn)
        update(kitaplar) 

    def yazaraGoreBul():
        yazar_adı = t3.get()
        kitaplar = kitaplar_listele.searchByAuthor(yazar_adı)
        update(kitaplar)

    def clear():
        kitaplar = kitaplar_listele.kitaplistele()
        update(kitaplar)
        kitap_adı_entry.delete("0",END)
        isbn_entry.delete("0",END)
        yazar_adı_entry.delete("0",END)

    yeniPencere = Toplevel()
    yeniPencere.title(secim + " Kitapları")
    yeniPencere.geometry("820x700")
    yeniPencere['background'] = '#1C2833'
   
    pgen = 820
    pyuks = 700

    ekrangen = yeniPencere.winfo_screenwidth()
    ekranyuks = yeniPencere.winfo_screenheight()

    x = (ekrangen - pgen) / 2
    y = (ekranyuks - pyuks) / 2

    yeniPencere.geometry("%dx%d+%d+%d"%(pgen, pyuks, x, y))

    wrapper1 = LabelFrame(yeniPencere,text= "BUL",height=60,bg="#1C2833", fg="yellow")
    wrapper2 = LabelFrame(yeniPencere,text="KİTAPLAR",height=120,bg="#1C2833", fg="yellow")
    wrapper3 = LabelFrame(yeniPencere,text="EMANET AL",height=60,bg="#1C2833", fg="yellow")
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=8)
    wrapper2.pack(fill="both",expand="yes",padx=20,pady=8)
    wrapper3.pack(fill="both",expand="yes",padx=20,pady=8)

    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()

    s1 = StringVar()
    s2 = StringVar()
    s3 = StringVar()
    s4 = StringVar()
    s5 = StringVar()
    s6 = StringVar()

    #Wrapper 1
    kitap_adı_lbl= Label(wrapper1, text="Kitap adı",bg="#1C2833", fg="yellow", font="Times 12 italic")
    kitap_adı_lbl.grid(row=0,column=0,padx=3,pady=3)
    kitap_adı_entry= Entry(wrapper1,textvariable=t1)
    kitap_adı_entry.grid(row=0,column=1,padx=3,pady=3)
    btn1 = Button(wrapper1,text="Ara",command= adaGoreBul,
                    bg= 'blue',fg='white',width=5)
    btn1.grid(row=0,column=2,padx=5,pady=3)

    isbn_lbl = Label(wrapper1,text="ISBN",bg="#1C2833", fg="yellow", font="Times 12 italic")
    isbn_lbl.grid(row=1,column=0,padx=5,pady=3)
    isbn_entry = Entry(wrapper1,textvariable=t2)
    isbn_entry.grid(row=1,column=1,padx=5,pady=3)
    btn2 = Button(wrapper1,text="Ara",command=ısbnGoreBul,
                    bg='blue',fg='white',width=5)
    btn2.grid(row=1,column=2,padx=5,pady=3)

    yazar_adı_lbl= Label(wrapper1, text="Yazar adı",bg="#1C2833", fg="yellow", font="Times 12 italic")
    yazar_adı_lbl.grid(row=2,column=0,padx=3,pady=3)
    yazar_adı_entry= Entry(wrapper1,textvariable=t3)
    yazar_adı_entry.grid(row=2,column=1,padx=3,pady=3)
    btn3 = Button(wrapper1,text="Ara",command= yazaraGoreBul,
                    bg= 'blue',fg='white',width=5)
    btn3.grid(row=2,column=2,padx=5,pady=3)

    kategori_lbl = Label(wrapper1,text="Kategoriler",
                        font='arial 10 bold')
    kategori_lbl.grid(row=0,column=3,padx=25,pady=2)
    kategoriListeleListbox = Listbox(wrapper1,width=30,height=10,relief="raised")
    kategoriListeleListbox.grid(row=1,column=3,columnspan=2,rowspan=4,
                                padx=50, pady=3)

    kategoriler = kategori.kategoriListele()
    for i in range(0,len(kategoriler)):
        kategoriListeleListbox.insert(END,kategoriler[i][1])

    kategoriListeleListbox.bind('<<ListboxSelect>>',items_selected)

    button_clear = Button(wrapper1,text="Filtre Temizle",command= clear,
                            fg="purple")
    button_clear.grid(row=0,column=5,padx=10,pady=3)                        

    #Wrapper 2
    style = ttk.Style()
    style.map('Treeview', background=[('selected', '#cc3300')])
    kitapListeleTree = Treeview(wrapper2,column=("1","2","3","4","5","6","7"), 
                                show='headings',height="4",
                                selectmode="browse")
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

    kitapListeleTree.column("#1",anchor = CENTER,width=100,minwidth = 110)
    kitapListeleTree.heading("#1",text="ISBN")

    kitapListeleTree.column("#2",anchor = CENTER,width=160,minwidth = 170)
    kitapListeleTree.heading("#2",text="Kitap")

    kitapListeleTree.column("#3",anchor = CENTER,width=120,minwidth = 130)
    kitapListeleTree.heading("#3",text="Yazar")

    kitapListeleTree.column("#4",anchor = CENTER,width=100,minwidth = 100)
    kitapListeleTree.heading("#4",text="Yayınevi")

    kitapListeleTree.column("#5",anchor = CENTER,width=100,minwidth = 110)
    kitapListeleTree.heading("#5",text="Basımyılı")

    kitapListeleTree.column("#6",anchor = CENTER,width=100,minwidth = 110)
    kitapListeleTree.heading("#6",text="Tür")

    kitapListeleTree.column("#7",anchor = CENTER,width=80,minwidth = 80)
    kitapListeleTree.heading("#7",text="Stok")

    kitapListeleTree.bind('<Double 1>',getrow)

    #Wrapper 3
    lbl_1= Label(wrapper3, text="ISBN",bg="#1C2833", fg="yellow", font="Times 14 italic")
    lbl_1.grid(row=0,column=0,padx=3,pady=3)
    entry_1= Entry(wrapper3,textvariable=s1,state='disabled')
    entry_1.grid(row=1,column=0,padx=3,pady=3)
        
    lbl_2= Label(wrapper3, text="Kitap adı",bg="#1C2833", fg="yellow", font="Times 14 italic")
    lbl_2.grid(row=0,column=1,padx=3,pady=3)
    entry_2= Entry(wrapper3,textvariable=s2,state='disabled')
    entry_2.grid(row=1,column=1,padx=3,pady=3)
        
    lbl_3= Label(wrapper3, text="yazarı",bg="#1C2833", fg="yellow", font="Times 14 italic")
    lbl_3.grid(row=0,column=2,padx=3,pady=3)
    entry_3= Entry(wrapper3,textvariable=s3,state='disabled')
    entry_3.grid(row=1,column=2,padx=3,pady=3)
        
    lbl_4= Label(wrapper3, text="Yayınevi",bg="#1C2833", fg="yellow", font="Times 14 italic")
    lbl_4.grid(row=2,column=0,padx=3,pady=3)
    entry_4= Entry(wrapper3,textvariable=s4,state='disabled')
    entry_4.grid(row=3,column=0,padx=3,pady=3)
        
    lbl_5= Label(wrapper3, text="Yayıntarihi",bg="#1C2833", fg="yellow", font="Times 14 italic")
    lbl_5.grid(row=2,column=1,padx=3,pady=3)
    entry_5= Entry(wrapper3,textvariable=s5,state='disabled')
    entry_5.grid(row=3,column=1,padx=3,pady=3)
        
    lbl_6= Label(wrapper3, text="Tür",bg="#1C2833", fg="yellow", font="Times 14 italic")
    lbl_6.grid(row=2,column=2,padx=3,pady=3)
    entry_6= Entry(wrapper3,textvariable=s6,state='disabled')
    entry_6.grid(row=3,column=2,padx=3,pady=3)

    emanet_btn = Button(wrapper3,text="Emanet al",fg='green', command = lambda : emanet.emanetAl(uyeID, entry_1.get(), kutuphaneID, yeniPencere, secim),
                        highlightcolor="green",highlightbackground="green",
                        highlightthickness=4,borderwidth=2)
    emanet_btn.grid(row=1,column=3,padx=8,pady=5)
    
    books = kitaplar_listele.kitaplistele2(kutuphaneID)
    update(books)
    
    # if secim == "A Kütüphanesi":
    #     listKutuphane_A = kitaplar_listele.kitaplistele()
    #     update(listKutuphane_A)
    # if secim == "B Kütüphanesi":
    #     listKutuphane_B = kitaplar_listele.kitaplistele()
    #     update(listKutuphane_B)
    # if secim == "C Kütüphanesi":
    #     listKutuphane_C = kitaplar_listele.kitaplistele()
    #     update(listKutuphane_C)

