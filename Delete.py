from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
from time import gmtime, strftime
import DB
import main

class delete_class:
    def __init__(self,id):
        self.id=id
        self.root=Tk()
        self.root.geometry("450x500+400+175")
        self.root.resizable(False,False)
        self.root.title("Delete Account Window")
        self.root.config(background="light blue")
        
       
        #Setting Up of content for window
        self.l0=Label(self.root,text='this is demo')
        self.l1=Label(self.root,text="Account No.",background="light blue")
        self.t1=Entry(self.root,width=30)
        self.b1=Button(self.root,text='Find',command=self.check)
        self.i1=ImageTk.PhotoImage(Image.open("images\\delete_account.png"))
        self.l0.config(image=self.i1,background="light blue")
        self.l0.place(relx=0.2,rely=0.05)
        self.l1.place(relx=0.2,rely=0.2)
        self.t1.place(relx=0.4,rely=0.2)
        self.b1.place(relx=0.5,rely=0.26)
        
        
        self.f1=Frame(self.root,height=240,width=500,background="light blue")
        
        self.l2=Label(self.f1,text="Name",background="light blue")
        self.l3=Label(self.f1,text="Address",background="light blue")
        self.l4=Label(self.f1,text="Gender",background="light blue")
        self.l5=Label(self.f1,text="Phone No.",background="light blue")
        self.l6=Label(self.f1,text="Email id",background="light blue") 
        self.l7=Label(self.f1,text="Balance",background="light blue")
        self.t2=Label(self.f1,width=30,background="light blue")
        self.t3=Label(self.f1,width=30,background="light blue")
        self.t4=Label(self.f1,width=30,background="light blue")
        self.t5=Label(self.f1,width=30,background="light blue")
        self.t6=Label(self.f1,width=30,background="light blue")
        self.t7=Label(self.f1,width=30,background="light blue")
        self.b2=Button(self.f1,text='Delete',command=self.check1)
        
        
        #placement of the photo
        
        self.l2.place(relx=0.09,rely=0.18)
        self.l3.place(relx=0.09,rely=0.28)
        self.l4.place(relx=0.09,rely=0.38)
        self.l5.place(relx=0.09,rely=0.48)
        self.l6.place(relx=0.09,rely=0.58)
        self.l7.place(relx=0.09,rely=0.68)
        
        self.t2.place(relx=0.27,rely=0.18)
        self.t3.place(relx=0.27,rely=0.28)
        self.t4.place(relx=0.27,rely=0.38)
        self.t5.place(relx=0.27,rely=0.48)
        self.t6.place(relx=0.27,rely=0.58)
        self.t7.place(relx=0.27,rely=0.68)
        self.b2.place(relx=0.36,rely=0.8)
        
        
        self.b3=Button(self.root,text="Back",command=self.back)
        self.b3.place(relx=0,rely=0)
        
        self.root.mainloop()
        
    def back(self):
        self.root.destroy()
        obj2=main.Main(self.id)
        
        
    def check(self):
        if(self.t1.get()!=""):
            row,r=DB.DBB().execute("select cname,caddress,cgender,cphno,cemail,odate,cbalance from tbuser where accno="+self.t1.get())
           
            if r>0:
                self.f1.place(relx=0.1,rely=0.32)
                
                self.t2.config(text=row[0])
                self.t3.config(text=row[1])
                self.t4.config(text=row[2])
                self.t5.config(text=row[3])
                self.t6.config(text=row[4])
                self.t7.config(text=row[6])
            else:   
                messagebox.showinfo("Info","No such record found")
        else:
            messagebox.showinfo("Info","Please enter the Account no")        
    def check1(self):
        m=messagebox.askyesno('Delete','Are You Sure you want to delete the account?')
        if(m):
            qry="delete from tbuser where accno="+self.t1.get()
            
            DB.DBB().execute(qry)
            messagebox.showinfo("Confirmation","Record Deleted Successfully")  
            self.root.destroy()
            obj2=main.Main(self.id)
        else:
            self.t1.delete(0,END)
            self.f1.place_forget()
