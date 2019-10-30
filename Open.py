from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
from time import gmtime, strftime
import DB
import main

class open_class:
    def __init__(self,id):
        self.id=id
        self.root=Tk()
        self.root.geometry("400x500+450+150")
        self.root.resizable(False,False)
        self.root.title("Main Window")
        self.root.config(background="light blue")
        
        self.accno=DB.DBB().accno()
        #Setting Up of content for window
        self.l0=Label(self.root)
        self.l1=Label(self.root,text="Account No.",background="light blue")
        self.l2=Label(self.root,text="Name",background="light blue")
        self.l3=Label(self.root,text="Address",background="light blue")
        self.l4=Label(self.root,text="Gender",background="light blue")
        self.l5=Label(self.root,text="Phone No.",background="light blue")
        self.l6=Label(self.root,text="Email id",background="light blue") 
        self.l7=Label(self.root,text="Balance",background="light blue")
        self.l11=Label(self.root,text=self.accno,background="light blue")
        self.t2=Entry(self.root,width=30)
        self.t3=Entry(self.root,width=30)
        self.t4=Entry(self.root,width=30)
        self.t5=Entry(self.root,width=30)
        self.t6=Entry(self.root,width=30)
        self.t7=Entry(self.root,width=30)
        self.b1=Button(self.root,text='Open',command=self.check)
        
        self.i1=ImageTk.PhotoImage(Image.open("images\\account_opening.png"))
        self.l0.config(image=self.i1,background="light blue")
        #placement of the photo
        self.l0.place(relx=0.12,rely=0.05)
        self.l1.place(relx=0.12,rely=0.2)
        self.l2.place(relx=0.12,rely=0.28)
        self.l3.place(relx=0.12,rely=0.36)
        self.l4.place(relx=0.12,rely=0.44)
        self.l5.place(relx=0.12,rely=0.52)
        self.l6.place(relx=0.12,rely=0.60)
        self.l7.place(relx=0.12,rely=0.68)
        
        self.l11.place(relx=0.52,rely=0.2)
        self.t2.place(relx=0.32,rely=0.28)
        self.t3.place(relx=0.32,rely=0.36)
        self.t4.place(relx=0.32,rely=0.44)
        self.t5.place(relx=0.32,rely=0.52)
        self.t6.place(relx=0.32,rely=0.60)
        self.t7.place(relx=0.32,rely=0.68)
        self.b1.place(relx=0.5,rely=0.8)
        
        self.b3=Button(self.root,text="Back",command=self.back)
        self.b3.place(relx=0,rely=0)
        
        self.root.mainloop()
        
    def back(self):
        self.root.destroy()
        obj2=main.Main(self.id)
        
    def check(self):
        if(self.t2.get()!="" and self.t3.get()!="" and self.t4.get()!="" and  self.t5.get()!="" and self.t6.get()!="" and self.t7.get()!=""):
            qry="insert into tbuser values('%s','%s','%s','%s',%s,'%s','%s',%s)"%(self.accno,self.t2.get(),self.t3.get(),self.t4.get(),self.t5.get(),self.t6.get(),strftime("%d-%m-%Y", gmtime()),self.t7.get())
            
            #print(qry)
            DB.DBB().insert(qry)
            messagebox.showinfo("Info","Account Opened Successfully")
            self.root.destroy()
            obj2=main.Main(self.id)
        else:
            messagebox.showinfo("Info","Please Enter All of the above columns")
