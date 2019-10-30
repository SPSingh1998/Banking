import threading
import time
from tkinter import *
from PIL import ImageTk,Image
from tkinter.ttk import Progressbar
import Login

class loading:
   
    def __init__(self):
        
        self.root=Tk()
        self.root.geometry("550x400+200+125")
        self.root.resizable(False,False)
        
        self.l1=Label(self.root,text="Welcome to Banking Solutions")
        self.i1=ImageTk.PhotoImage(Image.open("images\\logo1edited.png"))
        self.l1.config(image=self.i1)
        self.l1.pack(fill="both",expand="True")
        
        self.v1=IntVar()
        
        self.pb=Progressbar(self.root,orient=HORIZONTAL,length=550)
        self.pb.pack()
        self.pb.config(mode="determinate",maximum=100)
        self.pb.config(variable=self.v1)
        tup=(100,)
        self.t1=threading.Thread(target=self.show,args=tup,name="update_progress_bar")
        self.t1.start()
        self.root.after(500,self.check())
        self.root.mainloop()
        
    def check(self):
        if int(self.v1.get())==100:
            self.root.destroy()
            obj2=Login.Login_class1()
        else:
            self.root.after(500,self.check)

    def show(self,a):
        for i in range(a+1):
            self.v1.set(i)
            time.sleep(0.05)
            