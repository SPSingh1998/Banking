from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
import forgot_password
import main

class Login_class1:
    def __init__(self):
        
        self.root=Tk()
        self.root.geometry("600x400+200+125")
        self.root.config(background="light blue")
        self.root.resizable(False,False)
        
        self.l0=Label(self.root,text="Login Section")
        
        self.i1=ImageTk.PhotoImage(Image.open("images\\login_section1.png"))
        self.l0.config(image=self.i1,background="light blue")
        
        self.l1=Label(self.root,text="Username",background="light blue")
        self.l2=Label(self.root,text="Password",background="light blue")
        self.t1=Entry(self.root,width=30)
        self.t2=Entry(self.root,width=30,show="*")
        self.b1=Button(self.root,text="Login",command=self.login)
        self.b2=Button(self.root,text="Forgot Password",command=self.forgot)
        
        self.l0.place(relx=0.31,rely=0.05)
        self.l1.place(relx=0.3,rely=0.3)
        self.l2.place(relx=0.3,rely=0.4)
        self.t1.place(relx=0.42,rely=0.3)
        self.t2.place(relx=0.42,rely=0.4)
        self.b1.place(relx=0.5,rely=0.5)
        
        self.b2.place(relx=0.6,rely=0.6)
        
        self.root.mainloop()
        
    def login(self):
        conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=conn.cursor()
        id=self.t1.get();
        pwd=self.t2.get();
        if(id!="" and pwd!="" ):
            
            cursor.execute("select admid,admpwd from tbadmin where admid=%s and admpwd=%s",(id,pwd))
            r=cursor.rowcount;
            #print(r)
            if r>0:
                self.root.destroy()
                obj2=main.Main(id)
                
            
            else:
                messagebox.showinfo("Info","Invalid Username or Password")
            
        else:
            messagebox.showinfo("Info","Please Enter the Username and Password Field")
            self.t1.delete("1.0",END)
            self.t2.delete("1.0",END)
            
        conn.commit()
        conn.close()
            
    def forgot(self):
        self.root.destroy()
        obj1=forgot_password.forget()


#obj=Login_class1()
#ADD8E6