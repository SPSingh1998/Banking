from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
from time import gmtime, strftime
import DB
import main

class view_class:
   
    def __init__(self,id):
        self.id=id
        self.root=Tk()
        self.root.geometry("600x500+400+175")
        self.root.resizable(False,False)
        self.root.title("View All Account Window")
        self.root.config(background="light blue")
        
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        self.cursor=self.conn.cursor()
        
        self.l0=Label(self.root,text='this is demo')
        self.i1=ImageTk.PhotoImage(Image.open("images\\view_all_accounts.png"))
        self.l0.config(image=self.i1,background="light blue")
        self.l0.place(relx=0.2,rely=0.05)
        
        self.l11=Listbox(self.root,selectmode=SINGLE,height=40,width=30)
        qry="select * from tbuser"
        self.cursor.execute(qry)
        
        for row in self.cursor:
            self.l11.insert(END,str(row[0]))
        self.l11.bind("<<ListboxSelect>>", self.onSelect)
        self.l11.place(relx=0.72,rely=0.15)
        
        self.f1=Frame(self.root,height=240,width=360,background="light blue")
        self.l1=Label(self.f1,text="Account No",background="light blue")
        self.l2=Label(self.f1,text="Name",background="light blue")
        self.l3=Label(self.f1,text="Address",background="light blue")
        self.l4=Label(self.f1,text="Gender",background="light blue")
        self.l5=Label(self.f1,text="Phone No",background="light blue")
        self.l6=Label(self.f1,text="Email",background="light blue")
        self.l7=Label(self.f1,text="Opening Date",background="light blue")
        self.l8=Label(self.f1,text="Balance",background="light blue")
        
        self.t1=Label(self.f1,background="light blue")
        self.t2=Label(self.f1,background="light blue")
        self.t3=Label(self.f1,background="light blue")
        self.t4=Label(self.f1,background="light blue")
        self.t5=Label(self.f1,background="light blue")
        self.t6=Label(self.f1,background="light blue")
        self.t7=Label(self.f1,background="light blue")
        self.t8=Label(self.f1,background="light blue")
        
        self.l1.place(relx=0.09,rely=0.08)
        self.l2.place(relx=0.09,rely=0.18)
        self.l3.place(relx=0.09,rely=0.28)
        self.l4.place(relx=0.09,rely=0.38)
        self.l5.place(relx=0.09,rely=0.48)
        self.l6.place(relx=0.09,rely=0.58)
        self.l7.place(relx=0.09,rely=0.68)
        self.l8.place(relx=0.09,rely=0.78)
        
        self.t1.place(relx=0.4,rely=0.08)
        self.t2.place(relx=0.4,rely=0.18)
        self.t3.place(relx=0.4,rely=0.28)
        self.t4.place(relx=0.4,rely=0.38)
        self.t5.place(relx=0.4,rely=0.48)
        self.t6.place(relx=0.4,rely=0.58)
        self.t7.place(relx=0.4,rely=0.68)
        self.t8.place(relx=0.4,rely=0.78)
        
        self.b1=Button(self.root,text="Back",command=self.back)
        self.b1.place(relx=0,rely=0)
        
        self.root.mainloop()
    
    def back(self):
        self.root.destroy()
        obj2=main.Main(self.id)
    
    def onSelect(self,event):
        
        widget = event.widget
        selection=widget.curselection()
        
        value=str((widget.get(ANCHOR)))
        #print(qry)
        #print(value)
        self.cursor.execute("select * from tbuser where accno=%s",value)
        self.f1.place(relx=0.1,rely=0.15)
        r=self.cursor.rowcount
        row=self.cursor.fetchone()
        if r>0:
            self.t1.config(text=row[0])
            self.t2.config(text=row[1])
            self.t3.config(text=row[2])
            self.t4.config(text=row[3])
            self.t5.config(text=row[4])
            self.t6.config(text=row[5])
            self.t7.config(text=row[6])
            self.t8.config(text=row[7])
        else:
            messagebox.showinfo("Info","Internal Error")
        #print(selection)
        
        #print(event)
        
#obj=view_class("aa@gmail.com")