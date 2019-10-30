from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
from tkinter.ttk import Treeview
import DB
import main

class search_class:
    def __init__(self,id):
        self.id=id
        self.flag1=0
        self.flag2=0
        self.root=Tk()
        self.root.geometry("700x500+400+175")
        self.root.resizable(False,False)
        self.root.title("Search Window")
        self.root.config(background="light blue")
        
        self.l0=Label(self.root)
        self.i1=ImageTk.PhotoImage(Image.open("images\\search.png"))
        self.l0.config(image=self.i1,background="light blue")
        self.l0.place(relx=0.35,rely=0.02)
        
        self.l1=Label(self.root,text="Select Mode",background="light blue")
        self.l1.place(relx=0.25,rely=0.14)
        ls=('By Account No','By Name')
        self.s1=StringVar()
        self.s1.set('By Account No')
        self.c1=OptionMenu(self.root,self.s1,*ls)
        self.b1=Button(self.root,text='Show',command=self.onSelect)
        
        self.c1.place(relx=0.45,rely=0.14)
        self.b1.place(relx=0.4,rely=0.24)
        
        
        self.f1=Frame(self.root,height=400,width=445,background="light blue")
        self.l1=Label(self.f1,text='Account No',background='light blue')
        self.t1=Entry(self.f1,width=30)
        self.l1.place(relx=0.22,rely=0.02)
        self.t1.place(relx=0.4,rely=0.02)
        self.b2=Button(self.f1,text="Find",command=self.findacc)
        self.b2.place(relx=0.4,rely=0.1)
        #self.f1.place(relx=0.01,rely=0.3)
        
        self.f2=Frame(self.f1,height=200,width=445,background="light blue")
        self.l2=Label(self.f2,text="Name",background="light blue")
        self.l3=Label(self.f2,text="Address",background="light blue")
        self.l4=Label(self.f2,text="Gender",background="light blue")
        self.l5=Label(self.f2,text="Phone No",background="light blue")
        self.l6=Label(self.f2,text="Email",background="light blue")
        self.l7=Label(self.f2,text="Opening Date",background="light blue")
        self.l8=Label(self.f2,text="Balance",background="light blue")
        
        self.t2=Label(self.f2,background="light blue")
        self.t3=Label(self.f2,background="light blue")
        self.t4=Label(self.f2,background="light blue")
        self.t5=Label(self.f2,background="light blue")
        
        self.t6=Label(self.f2,background="light blue")
        self.t7=Label(self.f2,background="light blue")
        self.t8=Label(self.f2,background="light blue")
        
        self.l2.place(relx=0.14,rely=0.08)
        self.l3.place(relx=0.14,rely=0.18)
        self.l4.place(relx=0.14,rely=0.28)
        self.l5.place(relx=0.14,rely=0.38)
        self.l6.place(relx=0.14,rely=0.48)
        self.l7.place(relx=0.14,rely=0.58)
        self.l8.place(relx=0.14,rely=0.68)
        
        self.t2.place(relx=0.4,rely=0.08)
        self.t3.place(relx=0.4,rely=0.18)
        self.t4.place(relx=0.4,rely=0.28)
        self.t5.place(relx=0.4,rely=0.38)
        self.t6.place(relx=0.4,rely=0.48)
        self.t7.place(relx=0.4,rely=0.58)
        self.t8.place(relx=0.4,rely=0.68)
        
        #self.f2.place(relx=0.1,rely=0.2)
        
        
        #Layout for by name
        self.f3=Frame(self.root,height=400,width=700,background="light blue")
        self.label1=Label(self.f3,text="Account Holder's Name",background='light blue')
        self.entry1=Entry(self.f3,width=30)
        self.label1.place(relx=0.14,rely=0.02)
        self.entry1.place(relx=0.4,rely=0.02)
        self.button2=Button(self.f3,text="Find",command=self.findper)
        self.button2.place(relx=0.4,rely=0.1)
        
        self.f4=Frame(self.f3,height=200,width=445,background="light blue")
        self.text=Text(self.f4,height=20,width=85)
        
        self.text.grid(row=0,column=0)
        self.sc=Scrollbar(self.f4,orient=VERTICAL,command=self.text.yview)
        self.sc.grid(row=0,column=1,sticky='ns')
        self.text.config(yscrollcommand=self.sc.set)
        self.text.config(state="disabled")
        #self.f4.place(relx=0.1,rely=0.2)
        
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        self.cursor=self.conn.cursor()
        
        self.b3=Button(self.root,text="Back",command=self.back)
        self.b3.place(relx=0,rely=0)
        self.root.mainloop()
    
    def findper(self):
        if self.entry1.get()!="":
            self.cursor.execute("select * from tbuser where cname=%s",self.entry1.get())
            r=self.cursor.rowcount
            
            if r>0:
                self.f4.place(relx=0,rely=0.2)
                self.text.config(state='normal')
                self.text.delete('1.0',END)
                self.text.insert(END,"Name    Account No    Address    Gender    Phone No    Email Id    Opening Date\n")
                self.text.insert(END,"=====================================================================================\n")
                self.text.insert(END,"=====================================================================================\n")
                for row in self.cursor:
                    self.text.insert(END,row[1]+"       "+str(row[0])+"          "+row[2]+"        "+row[3]+"         "+str(row[4])+"        "+row[5]+"        "+row[6]+"\n")
                    self.text.insert(END,"=====================================================================================\n")
                self.text.config(state="disabled")
            else:
                messagebox.showinfo("Info","Internal Error")
                
        else:
            messagebox.showinfo("Info","Please Enter the field")
    
    def findacc(self):
        if self.t1.get()!='':
            self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
            self.cursor=self.conn.cursor()
            self.cursor.execute("select * from tbuser where accno=%s",self.t1.get())
            r=self.cursor.rowcount
            #print("Row Count is ; " , r)
            row=self.cursor.fetchone()
            #print(row)
            self.f2.place(relx=0.1,rely=0.2)
            if r>0:
                self.t2.config(text=row[1])
                self.t3.config(text=row[2])
                self.t4.config(text=row[3])
                self.t5.config(text=row[4])
                self.t6.config(text=row[5])
                self.t7.config(text=row[6])
                self.t8.config(text=row[7])
            else:
                messagebox.showinfo("Info","Internal Error")
                
        else:
            messagebox.showinfo("Info","Please Enter the field")
    def back(self):
        self.root.destroy()
        obj2=main.Main(self.id)
        
    def onSelect(self):
        
        if(self.s1.get()=='By Account No'):            
            if(self.flag1==1):
                self.f3.place_forget()
                self.flag2=0
            
            self.f1.place(relx=0.01,rely=0.3)
            self.flag1=1
        
        elif self.s1.get()=='By Name':
            if(self.flag1==1):
                self.f1.place_forget()
                self.flag1=0
            self.f3.place(relx=0,rely=0.3)
            self.flag2=1;
#obj=search_class("aa@gmail.com")