from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
from time import gmtime, strftime
import DB
import main

class mini_statement_class:
    def __init__(self,id):
        self.id=id
        self.root=Tk()
        self.root.geometry("550x500+400+175")
        self.root.resizable(False,False)
        self.root.title("Transfer Window")
        self.root.config(background="light blue")
        
       
        #Setting Up of content for window
        self.l0=Label(self.root,text='this is demo')
        self.l1=Label(self.root,text="Account No.",background="light blue")
        self.t1=Entry(self.root,width=30)
        self.b1=Button(self.root,text='Find',command=self.check)
        self.i1=ImageTk.PhotoImage(Image.open("images\\mini_statement.png"))
        self.l0.config(image=self.i1,background="light blue")
        self.l0.place(relx=0.2,rely=0.05)
        self.l1.place(relx=0.1,rely=0.2)
        self.t1.place(relx=0.4,rely=0.2)
        self.b1.place(relx=0.5,rely=0.26)
        
        self.f4=Frame(self.root,height=150,width=445,background="light blue")
        self.text=Text(self.f4,height=20,width=66)
        self.text.grid(row=0,column=0)
        self.sc=Scrollbar(self.f4,orient=VERTICAL,command=self.text.yview)
        self.sc.grid(row=0,column=1,sticky='ns')
        self.text.config(yscrollcommand=self.sc.set)
        self.text.config(state="disabled")
        
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        self.cursor=self.conn.cursor()
        
        self.b3=Button(self.root,text="Back",command=self.back)
        self.b3.place(relx=0,rely=0)
        
        self.root.mainloop()
    def back(self):
        self.root.destroy()
        obj2=main.Main(self.id)
    
    def check(self):
        if(self.t1.get()!=""):
            
            self.cursor.execute("select transamt,transtype,transdate,transtime from tbtransaction where transaccno=%s",self.t1.get())
            r=self.cursor.rowcount
           
            if r>0:
                
                self.f4.place(relx=0,rely=0.36)
                self.text.config(state='normal')
                self.text.delete('1.0',END)
                self.text.insert(END,"Trans Amt.     ||     Mode     ||     Date     ||     Time    \n")
                self.text.insert(END,"==================================================================\n")
                self.text.insert(END,"==================================================================\n")
                
                for row in self.cursor:
                    
                    self.text.insert(END,str(row[0])+"                "+row[1]+"         "+row[2]+"        "+row[3]+"\n")
                    self.text.insert(END,"==================================================================\n")
                self.text.config(state="disabled")
                self.t1.config(state="disabled")
                
            else:   
                messagebox.showinfo("Info","No such record found")
        else:
            messagebox.showinfo("Info","Please enter the Account no")
            
            
            
            
