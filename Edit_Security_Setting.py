from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
from time import gmtime, strftime
import DB
import main

class edit_security_setting_class():
    def __init__(self,id):
        
        self.id=id
        self.root=Tk()
        self.root.geometry("450x500+400+175")
        self.root.resizable(False,False)
        self.root.title("Security Question Window")
        self.root.config(background="light blue")
        
        
        #Setting Up of content for window
        self.l0=Label(self.root,text='this is demo')
        self.i1=ImageTk.PhotoImage(Image.open("images\\edit_security_settings.png"))
        self.l0.config(image=self.i1,background="light blue")
        self.l0.place(relx=0.1,rely=0.05)
        
        self.l2=Label(self.root,text="Security Question",background="light blue")
        self.l3=Label(self.root,text="Security Answer",background="light blue")
        self.l4=Label(self.root,text="New Security Question",background="light blue")
        self.l5=Label(self.root,text="New Security Answer",background="light blue")
        
        self.t2=Label(self.root,background="light blue")
        self.t3=Entry(self.root,width=30,show='*')
        self.t4=Entry(self.root,width=30)
        self.t5=Entry(self.root,width=30,show='*')
        
        self.b2=Button(self.root,text='Update',command=self.check1)
        
        qry="select admsecques from tbadmin where admid='%s'"%(self.id)
        
        row,r=DB.DBB().execute(qry)
        self.t2.config(text=row[0])
        
        
        
        #placement of the photo
        
        self.l2.place(relx=0.09,rely=0.28)
        self.l3.place(relx=0.09,rely=0.38)
        self.l4.place(relx=0.09,rely=0.48)
        self.l5.place(relx=0.09,rely=0.58)
        
        self.t2.place(relx=0.4,rely=0.28)
        self.t3.place(relx=0.4,rely=0.38)
        self.t4.place(relx=0.4,rely=0.48)
        self.t5.place(relx=0.4,rely=0.58)
        self.b2.place(relx=0.4,rely=0.8)
        
        
        self.b3=Button(self.root,text="Back",command=self.back)
        self.b3.place(relx=0,rely=0)
        
        self.root.mainloop()
        
    def back(self):
        self.root.destroy()
        obj2=main.Main(self.id)
        
    
                
    def check1(self):
        if(self.t5.get()!="" and self.t3.get()!="" and self.t4.get()!=""):
            qry="select admpwd from tbadmin where admid='%s' and admsecans='%s'"%(self.id,self.t3.get())
            row,r=DB.DBB().execute(qry)
            if r>0:
                
                qry="update tbadmin set admsecques='%s',admsecans='%s' where admid='%s'"%(self.t4.get(),self.t5.get(),self.id)
                DB.DBB().execute(qry)
                messagebox.showinfo("Info","Password Changed Successfully")
                self.root.destroy()
                obj2=main.Main(self.id)
                
            else:
                messagebox.showinfo("Error","Security Answer does not match with record")
        else:
            messagebox.showinfo("Info","Please Enter All of the above columns")
            
        
#obj=edit_security_setting_class("aa@gmail.com")