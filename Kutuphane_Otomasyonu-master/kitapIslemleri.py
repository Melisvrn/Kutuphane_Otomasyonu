from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter.font import BOLD
from tkinter.ttk import Treeview
import kitap_emanet_teslim

#backgroundcolors = SlateGray3,SlateGray4, DarkSeaGreen3,DarkSeaGreen4,#33334d
#yazı rengi = #ff9900,#009999,#99004d,#cc3300
#-#009999-mavi
#-#993399-mor
#-#339966-yesil
#-#99004d-pembe-kırmızı
#-#ff9900-sarı-turuncu
#-#33334d-koyu gri


def kitapGecmisi(uyeID):
    yeniPencere = Tk()
    yeniPencere.title("Deneme")
    yeniPencere.geometry("820x700")
    yeniPencere['background'] = '#1C2833'

    pgen = 820
    pyuks = 700

    ekrangen = yeniPencere.winfo_screenwidth()
    ekranyuks = yeniPencere.winfo_screenheight()

    x = (ekrangen - pgen) / 2
    y = (ekranyuks - pyuks) / 2

    yeniPencere.geometry("%dx%d+%d+%d" % (pgen, pyuks, x, y))


    wrapper1 = LabelFrame(yeniPencere, bg="#1C2833", fg="yellow",
                        highlightbackground="yellow", highlightcolor="yellow", highlightthickness=1, bd=1)
    wrapper2 = LabelFrame(yeniPencere, height=120, bg="#1C2833", fg="yellow",
                        highlightbackground="yellow", highlightcolor="yellow", highlightthickness=1, bd=1)
    wrapper3 = LabelFrame(yeniPencere, height=60, bg="#1C2833", fg="yellow",
                        highlightbackground="yellow", highlightcolor="yellow", highlightthickness=1, bd=1)
    wrapper1.pack(fill="both", expand="yes", padx=20, pady=8)
    Label(yeniPencere, text="Emanet Alınmış Kitaplar",
        bg="#1C2833", fg="yellow", font="Times 14 italic").pack()
    wrapper2.pack(fill="both", expand="yes", padx=20, pady=8)
    Label(yeniPencere, text="Teslim Edilmiş Kitaplar",
        bg="#1C2833", fg="yellow", font="Times 14 italic").pack()
    wrapper3.pack(fill="both", expand="yes", padx=20, pady=8)

    #-----------------------------
    style = ttk.Style()
    # tema belirleme : default,alt,clam,visca
    # style.theme_use("default")
    #select rengi belirme
    style.map('Treeview', background=[('selected', '#cc3300')])
    #-------------------------------

    # Wrapper 1
    s1 = StringVar(wrapper1,kitap_emanet_teslim.emaneAlinanKitaplarSayısı(uyeID))
    s2 = StringVar(wrapper1,kitap_emanet_teslim.teslimEdilenKitaplarSayısı(uyeID))
    entry_1 = Entry(wrapper1, textvariable=s1,
                    state='disabled', fg="black",
                    font="Times 22 bold", highlightthickness=2, width=8, justify="center")
    entry_1.grid(row=0, column=0, padx=100, pady=10, ipady=30)
    entry_1.config(highlightbackground="yellow", highlightcolor="yellow")
    entry_2 = Entry(wrapper1, textvariable=s2,
                    state='disabled', fg="black",
                    font="Times 22 bold", highlightthickness=2, width=8, justify="center")
    entry_2.grid(row=0, column=1, padx=100, pady=10, ipady=30)
    entry_2.config(highlightbackground="yellow", highlightcolor="yellow")

    lbl_1 = Label(wrapper1, text="Emanet alınan",
                bg="yellow", font="Times 12 italic")
    lbl_1.grid(row=1, column=0, padx=3, pady=3)
    lbl_2 = Label(wrapper1, text="Teslim edilen",
                bg="yellow", font="Times 12 italic")
    lbl_2.grid(row=1, column=1, padx=3, pady=3)


    # Wrapper 2
    kitapListeleTree = Treeview(wrapper2, column=("1", "2", "3", "4","5","6"),
                                show='headings', height="7",
                                selectmode="none")
    kitapListeleTree.pack(side="left")
    kitapListeleTree.place(x=0, y=0)

    # vertical scrollbar
    yscroolbar = Scrollbar(wrapper2, orient="vertical",
                        command=kitapListeleTree.yview)
    yscroolbar.pack(side='right', fill=Y)


    kitapListeleTree.config(yscrollcommand=yscroolbar.set)

    kitapListeleTree.column("#1", anchor=CENTER, width=120, minwidth=60)
    kitapListeleTree.heading("#1", text="ISBN")

    kitapListeleTree.column("#2", anchor=CENTER, width=150, minwidth=100)
    kitapListeleTree.heading("#2", text="Kitap")

    kitapListeleTree.column("#3", anchor=CENTER, width=150, minwidth=60)
    kitapListeleTree.heading("#3", text="Üye")

    kitapListeleTree.column("#4", anchor=CENTER, width=140, minwidth=100)
    kitapListeleTree.heading("#4", text="Kütüphane")

    kitapListeleTree.column("#5", anchor=CENTER, width=100, minwidth=80)
    kitapListeleTree.heading("#5", text="Alım Tarihi")

    kitapListeleTree.column("#6", anchor=CENTER, width=100, minwidth=80)
    kitapListeleTree.heading("#6", text="Teslim Tarihi")

    kitaplar = kitap_emanet_teslim.emaneAlinanKitaplar(uyeID)
    for i in range(len(kitaplar)):
        kitapListeleTree.insert('', 'end', values=kitaplar[i])
        
    
    

    # Wrapper 3
    kitapListeleTree = Treeview(wrapper3, column=("1", "2", "3", "4", "5", "6"),
                                show='headings', height="7",
                                selectmode="none")
    kitapListeleTree.pack(side="left")
    kitapListeleTree.place(x=0, y=0)

    # vertical scrollbar
    yscroolbar = Scrollbar(wrapper3, orient="vertical",
                        command=kitapListeleTree.yview)
    yscroolbar.pack(side='right', fill=Y)

    kitapListeleTree.config(yscrollcommand=yscroolbar.set)

    kitapListeleTree.column("#1", anchor=CENTER, width=120, minwidth=60)
    kitapListeleTree.heading("#1", text="ISBN")

    kitapListeleTree.column("#2", anchor=CENTER, width=150, minwidth=100)
    kitapListeleTree.heading("#2", text="Kitap")

    kitapListeleTree.column("#3", anchor=CENTER, width=150, minwidth=60)
    kitapListeleTree.heading("#3", text="Üye")

    kitapListeleTree.column("#4", anchor=CENTER, width=140, minwidth=100)
    kitapListeleTree.heading("#4", text="Kütüphane")

    kitapListeleTree.column("#5", anchor=CENTER, width=100, minwidth=80)
    kitapListeleTree.heading("#5", text="Alım Tarihi")

    kitapListeleTree.column("#6", anchor=CENTER, width=100, minwidth=80)
    kitapListeleTree.heading("#6", text="Teslim Tarihi")

    kitaplar = kitap_emanet_teslim.teslimEdilenKitaplar(uyeID)
    
    for i in range(len(kitaplar)):
        kitapListeleTree.insert('', 'end', values=kitaplar[i])





