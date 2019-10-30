from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
from time import gmtime, strftime
import DB
import main

class edit_password_class():
    def __init__(self,id):
        
        self.id=id
        self.root=Tk()
        self.root.geometry("450x500+400+150")
        self.root.resizable(False,False)
        self.root.title("Edit Profile Window")
        self.root.config(background="light blue")
        
        #Setting Up of content for window
        self.l0=Label(self.root,text='this is demo')
        self.i1=ImageTk.PhotoImage(Image.open("images\\edit_password.png"))
        self.l0.config(image=self.i1,background="light blue")
        self.l0.place(relx=0.3,rely=0.05)
        
        self.l2=Label(self.root,text="Old Password",background="light blue")
        self.l3=Label(self.root,text="New Password",background="light blue")
        self.l4=Label(self.root,text="Confirm Password",background="light blue")
        
        self.t2=Entry(self.root,width=30,show='*')
        self.t3=Entry(self.root,width=30,show='*')
        self.t4=Entry(self.root,width=30,show='*')
        
        self.b2=Button(self.root,text='Update',command=self.check1)
        
        #placement of the photo
        
        self.l2.place(relx=0.09,rely=0.18)
        self.l3.place(relx=0.09,rely=0.28)
        self.l4.place(relx=0.09,rely=0.38)
        
        self.t2.place(relx=0.35,rely=0.18)
        self.t3.place(relx=0.35,rely=0.28)
        self.t4.place(relx=0.35,rely=0.38)
        
        self.b2.place(relx=0.45,rely=0.5)
        
        self.b3=Button(self.root,text="Back",command=self.back)
        self.b3.place(relx=0,rely=0)
        
        self.root.mainloop()
        
    def back(self):
        self.root.destroy()
        obj2=main.Main(self.id)
        
                
    def check1(self):
        if(self.t2.get()!="" and self.t3.get()!="" and self.t4.get()!=""):
            qry="select admpwd from tbadmin where admid='%s' and admpwd='%s'"%(self.id,self.t2.get())
            row,r=DB.DBB().execute(qry)
            if r>0:
                if self.t3.get()==self.t4.get():
                    qry="update tbadmin set admpwd='%s'where admid='%s'"%(self.t3.get(),self.id)
                    
                    DB.DBB().execute(qry)
                    messagebox.showinfo("Info","Password Changed Successfully")
                    self.root.destroy()
                    obj2=main.Main(self.id)
                else:
                    messagebox.showinfo("Info","New Password And Confirm Password should be same")
            else:
                messagebox.showinfo("Error","Password does not match with record")
        else:
            messagebox.showinfo("Info","Please Enter All of the above columns")
