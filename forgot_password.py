from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
import Login

class forget:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("600x400+200+125")
        self.root.config(background="light blue")
        self.root.resizable(False,False)
        
        self.l0=Label(self.root,text="Login Section")
        
        self.i1=ImageTk.PhotoImage(Image.open("images\\forgot_password.png"))
        self.l0.config(image=self.i1,background="light blue")
        
        self.l1=Label(self.root,text="Username",background="light blue")
        self.t1=Entry(self.root,width=30)
        self.b1=Button(self.root,text="Verify",command=self.verify)
        self.l0.place(relx=0.31,rely=0.05)
        self.l1.place(relx=0.3,rely=0.22)
        self.t1.place(relx=0.4,rely=0.22)
        self.b1.place(relx=0.5,rely=0.3)
        
        #FRAME 1
        self.f1=Frame(self.root,height=240,width=500,background="light blue")
        
        self.l2=Label(self.f1,text="Security Question",background="light blue")
        self.secq=Label(self.f1,background="light blue")
        self.l3=Label(self.f1,text="Security Answer",background="light blue")
        self.t3=Entry(self.f1,width=30,show="*")
        self.b2=Button(self.f1,text="Verify",command=self.verify2)
        
        self.l2.place(relx=0.16,rely=0.05)
        self.secq.place(relx=0.36,rely=0.05)
        self.l3.place(relx=0.18,rely=0.15)
        self.t3.place(relx=0.36,rely=0.15)
        self.b2.place(relx=0.48,rely=0.28)
        
        #self.f1.place(relx=0.1,rely=0.4)
        
        #FRAME 2
        self.f2=Frame(self.f1,height=240,width=500,background="light blue")
        
        self.l4=Label(self.f2,text="New Password",background="light blue")
        self.t4=Entry(self.f2,width=30,show="*")
        self.l5=Label(self.f2,text="Confirm New Password",background="light blue")
        self.t5=Entry(self.f2,width=30,show="*")
        self.b3=Button(self.f2,text="Verify",command=self.verify3)
        
        self.l4.place(relx=0.19,rely=0.05)
        self.t4.place(relx=0.36,rely=0.05)
        self.l5.place(relx=0.1,rely=0.15)
        self.t5.place(relx=0.36,rely=0.15)
        self.b3.place(relx=0.48,rely=0.28)
        
        #self.f2.place(relx=0.001,rely=0.43)
        
        self.root.mainloop()
        
    def verify(self):
        conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=conn.cursor()
        self.id=self.t1.get()
        if(id!=""):
            
            cursor.execute("select admsecques from tbadmin where admid=%s",(self.id))
            r=cursor.rowcount
            if r>0:
                row=cursor.fetchone()
                self.secq.config(text=row[0])
                self.f1.place(relx=0.1,rely=0.4)
                self.t1.config(stat='disabled')
            
            else:
                messagebox.showinfo("Info","Invalid Username")
                self.t1.delete(0,END)
            
        else:
            messagebox.showinfo("Info","Please Enter the Username")
        conn.commit()
        conn.close()
        
    def verify2(self):
        conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=conn.cursor()
        ans=self.t3.get()
        if(ans!=""):
            
            cursor.execute("select admsecans from tbadmin where admid=%s and admsecans=%s",(self.id,ans))
            r=cursor.rowcount
            if r>0:
                self.f2.place(relx=0.001,rely=0.43)
                self.t3.config(state='disabled')
            
            else:
                messagebox.showinfo("Info","Your Answer is wrong")
                self.t3.delete(0,END)
            
        else:
            messagebox.showinfo("Info","Please Enter the Answer")
        conn.commit()
        conn.close()
        
     
    def verify3(self):
        conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=conn.cursor()
        np=self.t4.get()
        cnp=self.t5.get()
        if(np!="" and cnp!=""):
            
            if(np==cnp):
                cursor.execute("update tbadmin set admpwd=%s where admid=%s",(np,self.id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password Changed Successfully")
                self.root.destroy()
                
                obj=Login.Login_class1()
                
            else:
                messagebox.showinfo("Info","Password should be same in both the fields")
                self.t4.delete(0,END)
                self.t5.delete(0,END)

        else:
            messagebox.showinfo("Info","Please Enter the Password in Both the fields")
        
            
#obj=forget()    