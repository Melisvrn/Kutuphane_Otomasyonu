from tkinter import *
from tkinter import messagebox
import kutuphaneler
import uyelikIslemleri

pencere = Tk()
pencere.title("KÜTÜPHANE")
pencere.geometry("350x370")
pencere['background'] = '#1C2833'

pgen = 400
pyuks = 370


ekrangen = pencere.winfo_screenwidth()
ekranyuks = pencere.winfo_screenheight()

x = (ekrangen - pgen) / 2
y = (ekranyuks - pyuks) / 2

pencere.geometry("%dx%d+%d+%d"%(pgen, pyuks, x, y))

def bilgilendirme():
    messagebox.showinfo("Bilgilendirme", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

def uyeGiris_uyeKayit():
    musteriButton = Button(pencere, text = "Giriş İşlemleri", width = 17, height = 5,bg="#cc3300",fg="white",font="Times 10 bold" ,command = uyelikIslemleri.uyelikIslemleriEkrani)
    musteriButton.grid(padx = 130, pady = 75)
    bilgilendirmeButton = Button(pencere, text = "Bilgilendirme", width = 17, height = 5,bg="#99004d",fg="white",font="Times 10 bold" ,command = bilgilendirme)
    bilgilendirmeButton.grid(padx = 130, pady = 25)

def main():
    uyeGiris_uyeKayit()
    pencere.mainloop()
    

if __name__ == "__main__":
    main()
