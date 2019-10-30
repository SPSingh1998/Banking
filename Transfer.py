from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
from time import gmtime, strftime
import DB
import main

class transfer_class:
    def __init__(self,id):
        self.id=id
        self.root=Tk()
        self.root.geometry("450x500+400+175")
        self.root.resizable(False,False)
        self.root.title("Transfer Window")
        self.root.config(background="light blue")
        
       
        #Setting Up of content for window
        self.l0=Label(self.root,text='this is demo')
        self.l1=Label(self.root,text="Sender Account No.",background="light blue")
        self.t1=Entry(self.root,width=30)
        self.b1=Button(self.root,text='Find',command=self.check)
        self.i1=ImageTk.PhotoImage(Image.open("images\\withdraw.png"))
        self.l0.config(image=self.i1,background="light blue")
        self.l0.place(relx=0.3,rely=0.05)
        self.l1.place(relx=0.1,rely=0.2)
        self.t1.place(relx=0.4,rely=0.2)
        self.b1.place(relx=0.5,rely=0.26)
        
        self.f0=Frame(self.root,height=240,width=500,background="light blue")
        self.l11=Label(self.f0,text="Receiver Account No.",background="light blue")
        self.t11=Entry(self.f0,width=30)
        self.b11=Button(self.f0,text='Find',command=self.find)
        self.l11.place(relx=0.1,rely=0.1)
        self.t11.place(relx=0.36,rely=0.1)
        self.b11.place(relx=0.45,rely=0.2)
        #self.f0.place(relx=0,rely=0.36)
        
        self.f1=Frame(self.f0,height=240,width=500,background="light blue")
        self.l2=Label(self.f1,text="Transfer Amount",background="light blue")
        self.t2=Entry(self.f1,width=30)
        self.b2=Button(self.f1,text='Transfer',command=self.withdraw)
        self.l2.place(relx=0.1,rely=0.1)
        self.t2.place(relx=0.35,rely=0.1)
        self.b2.place(relx=0.45,rely=0.2)
        
        self.b3=Button(self.root,text="Back",command=self.back)
        self.b3.place(relx=0,rely=0)
        
        self.root.mainloop()
        
    def back(self):
        self.root.destroy()
        obj2=main.Main(self.id)
        
    
    def find(self):
        if(self.t11.get()!=""):
            if self.t11.get()==self.t1.get():
                messagebox.showinfo("Error","Sender and Receiver's Account number are same")
                self.t11.delete(0, END)
            else:
                row,r=DB.DBB().execute("select accno from tbuser where accno="+self.t11.get())
            
                if r>0:
                    self.f1.place(relx=0,rely=0.36)        
                    self.t11.config(state="disabled")
                else:   
                    messagebox.showinfo("Info","No such record found")
        else:
            messagebox.showinfo("Info","Please enter the Receivers Account no")
    
    def withdraw(self):
        if(self.t2.get()!=""):
            row,r=DB.DBB().execute("select cbalance from tbuser where accno="+self.t1.get())
            row1,r1=DB.DBB().execute("select cbalance from tbuser where accno="+self.t11.get())
            if r>0 and r1>0:
                if row[0]>(int(self.t2.get())+500):
                    amt=row[0]-int(self.t2.get())
                    #print(qry)
                    qry="update tbuser set cbalance=%s where accno=%s"%(amt,self.t1.get())
                    DB.DBB().insert(qry)
                    
                    amt1=row1[0]+int(self.t2.get())
                    #print(qry)
                    qry="update tbuser set cbalance=%s where accno=%s"%(amt1,self.t11.get())
                    DB.DBB().insert(qry)
                    
                    t=DB.DBB().transid()
                    
                    qry='insert into tbtransaction values(%s,%s,"Transfer",%s,"%s","%s")'%(t,self.t1.get(),self.t2.get(),strftime("%d-%m-%Y", gmtime()),strftime("%H:%M:%S", gmtime()))
                    #print(qry)
                    DB.DBB().insert(qry)
                    
                    qry='insert into tbtransaction values(%s,%s,"Transfer",%s,"%s","%s")'%(t+1,self.t11.get(),self.t2.get(),strftime("%d-%m-%Y", gmtime()),strftime("%H:%M:%S", gmtime()))
                    #print(qry)
                    DB.DBB().insert(qry)
                    
                    messagebox.showinfo("Transaction Successfull"," Sender's New Balance="+str(amt))
                    self.root.destroy()
                    obj2=main.Main(self.id)
                else:
                    messagebox.showinfo("Transaction Failed","Not Sufficient Balance in account")
            else:   
                messagebox.showerror("Error","Internal Error")
        else:
            messagebox.showinfo("Info","Please enter the withdrawal amount")
        
    def check(self):
        if(self.t1.get()!=""):
            row,r=DB.DBB().execute("select accno from tbuser where accno="+self.t1.get())
           
            if r>0:
                self.f0.place(relx=0,rely=0.36)
                
                self.t1.config(state="disabled")
            else:   
                messagebox.showinfo("Info","No such record found")
        else:
            messagebox.showinfo("Info","Please enter the Sender Account no")   

        