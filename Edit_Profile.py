from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
from time import gmtime, strftime
import DB
import main

class edit_profile_class():
    def __init__(self,id):
        
        self.id=id
        self.root=Tk()
        self.root.geometry("450x500+400+175")
        self.root.resizable(False,False)
        self.root.title("Edit Profile Window")
        self.root.config(background="light blue")
        
        
        #Setting Up of content for window
        self.l0=Label(self.root,text='this is demo')
        self.i1=ImageTk.PhotoImage(Image.open("images\\edit_profile.png"))
        self.l0.config(image=self.i1,background="light blue")
        self.l0.place(relx=0.2,rely=0.05)
        
        self.l2=Label(self.root,text="Name",background="light blue")
        self.l3=Label(self.root,text="Address",background="light blue")
        self.l4=Label(self.root,text="Gender",background="light blue")
        self.l5=Label(self.root,text="Phone No.",background="light blue")
        
        self.t2=Entry(self.root,width=30)
        self.t3=Entry(self.root,width=30)
        self.t4=Entry(self.root,width=30)
        self.t5=Entry(self.root,width=30)
        
        self.b2=Button(self.root,text='Update',command=self.check1)
        
        qry="select admname,admaddress,admgender,admphno from tbadmin where admid='%s'"%(self.id)
        
        row,r=DB.DBB().execute(qry)
        self.t2.insert(0,row[0])
        self.t3.insert(0,row[1])
        self.t4.insert(0,row[2])
        self.t5.insert(0,row[3])
        
        
        #placement of the photo
        
        self.l2.place(relx=0.1,rely=0.18)
        self.l3.place(relx=0.1,rely=0.28)
        self.l4.place(relx=0.1,rely=0.38)
        self.l5.place(relx=0.1,rely=0.48)
        
        self.t2.place(relx=0.28,rely=0.18)
        self.t3.place(relx=0.28,rely=0.28)
        self.t4.place(relx=0.28,rely=0.38)
        self.t5.place(relx=0.28,rely=0.48)
        self.b2.place(relx=0.36,rely=0.6)
        
        
        self.b3=Button(self.root,text="Back",command=self.back)
        self.b3.place(relx=0,rely=0)
        
        self.root.mainloop()
        
    def back(self):
        self.root.destroy()
        obj2=main.Main(self.id)
        
                
    def check1(self):
        if(self.t2.get()!="" and self.t3.get()!="" and self.t4.get()!="" and  self.t5.get()!=""):
            qry="update tbadmin set admname='%s',admaddress='%s',admgender='%s',admphno=%s where admid='%s'"%(self.t2.get(),self.t3.get(),self.t4.get(),self.t5.get(),self.id)
            #print(qry)
            DB.DBB().execute(qry)
            messagebox.showinfo("Info","Data Modified Successfully")
            self.root.destroy()
            obj2=main.Main(self.id)
            
        else:
            messagebox.showinfo("Info","Please Enter All of the above columns")
