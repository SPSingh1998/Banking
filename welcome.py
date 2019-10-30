from tkinter import *
from PIL import Image,ImageTk
from Loading import loading
class Welcome:
    def __init__(self):
        
        self.root=Tk()
        self.root.geometry("900x500+200+125")
        self.root.resizable(False,False)
        self.root.config(background="light yellow")
        
        self.l1=Label(self.root,text="Welcome to Banking Solutions")
        self.i1=ImageTk.PhotoImage(Image.open("images\\Logo.png"))
        self.l1.config(image=self.i1)
        self.l1.pack(fill="both",expand="True")
        
        self.b1=Button(self.root,text="Click Here To Continue",command=self.action)
        self.b1.pack()
        self.root.mainloop()

    def action(self):
        self.root.destroy()
        obj2=loading()
        pass
obj=Welcome()