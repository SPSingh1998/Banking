from tkinter import *
import main
from PIL import ImageTk,Image
import main
class about_us:
    def __init__(self,id):
        self.id=id
        self.root=Tk()
        self.root.config(background="white")
        self.root.geometry("800x500+200+125")
        self.l0=Label(self.root)
        self.i0=ImageTk.PhotoImage(Image.open("images\\MADE_BY_-.png"))
        self.l0.config(image=self.i0,background="white")
        
        self.l1=Label(self.root)
        self.i1=ImageTk.PhotoImage(Image.open("images\\SUMIT PAL SINGH.png"))
        self.l1.config(image=self.i1,background="white")
        
        self.l2=Label(self.root)
        self.i2=ImageTk.PhotoImage(Image.open("images\\FDA.png"))
        self.l2.config(image=self.i2,background="white")
        
        self.l3=Label(self.root)
        self.i3=ImageTk.PhotoImage(Image.open("images\\ER.png"))
        self.l3.config(image=self.i3,background="white")
        
        self.l4=Label(self.root)
        self.i4=ImageTk.PhotoImage(Image.open("images\\TECHSQUARE.png"))
        self.l4.config(image=self.i4,background="white")
        
        self.l0.pack()
        self.l1.pack()
        self.l2.pack()
        self.l3.pack()
        self.l4.pack()
        
        self.b1=Button(self.root,text='back',command=self.back)
        self.b1.place(relx=0,rely=0)
        
        self.root.mainloop()
    
    def back(self):
        self.root.destroy()
        obj2=main.Main(self.id)
#obj=about_us("aa@gmail.com")