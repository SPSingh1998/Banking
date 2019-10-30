from pymysql import cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql.cursors
import Open
import Modify
import Delete
import View
import Withdraw
import Deposit
import Transfer
import Mini_Statement
import Edit_Password
import Edit_Profile
import Edit_Security_Setting
import Login
import Search
import aboutus
class Main:
    def __init__(self,id):
        self.id=id
        self.root=Tk()
        self.root.geometry("900x500+200+125")
        self.root.resizable(False,False)
        self.root.option_add('*tearOff', False)
        self.root.title("Main Window")
        self.root.config(background='#e1e1e1')
        self.menu=Menu(self.root)
        self.root.config(menu=self.menu)
        self.t1=Text(self.root)
        self.l0=Label(self.root)
        self.i1=ImageTk.PhotoImage(Image.open("images\\logo1edited.png"))
        self.l0.config(image=self.i1,background="#e1e1e1")
        self.l0.place(relx=0.15,rely=0.15)
        #Menu in Menubar
        self.account=Menu(self.menu)
        self.transaction=Menu(self.menu)
        self.admin=Menu(self.menu)
        self.help=Menu(self.menu)
        self.menu.add_cascade(menu=self.account,label="Account")
        self.menu.add_cascade(menu=self.transaction,label="Transaction")
        self.menu.add_cascade(menu=self.admin,label="Admin")
        self.menu.add_cascade(menu=self.help,label='Help')
        
        #Menu Items in Menu Account
        
        self.account.add_command(label='Open New Account',command=self.open)
        self.account.add_command(label='Modify Account',command=self.modify)
        self.account.add_command(label='Delete Account',command=self.delete)
        self.account.add_command(label='View All Account',command=self.view)
        self.account.add_command(label='Search',command=self.search)
        
        
        #Menu Items in Menu Transaction
        self.transaction.add_command(label='Withdraw',command=self.withdraw)
        self.transaction.add_command(label='Deposit',command=self.deposit)
        self.transaction.add_command(label='Transfer',command=self.transfer)
        self.transaction.add_command(label='Mini Statement',command=self.mini)
        
        #Menu items in Menu Admin
        self.admin.add_command(label='Edit Profile',command=self.edit_profile)
        self.admin.add_command(label='Edit Password',command=self.edit_password)
        self.admin.add_command(label="Edit Security Settings",command=self.edit_security)
        self.admin.add_separator()
        self.admin.add_command(label='Logout',command=self.logout)
        
        #Menu items in Help
        self.help.add_command(label='About Us',command=self.about) 
        self.root.mainloop()
        
    def open(self):
        self.root.destroy()
        obj2=Open.open_class(self.id)
        
    def modify(self):
        self.root.destroy()
        obj2=Modify.modify_class(self.id)
    
    def delete(self):
        self.root.destroy()
        obj2=Delete.delete_class(self.id)
    
    def view(self):
        self.root.destroy()
        obj2=View.view_class(self.id)
    def withdraw(self):
        self.root.destroy()
        obj2=Withdraw.withdraw_class(self.id)
    def deposit(self):    
        self.root.destroy()
        obj2=Deposit.deposit_class(self.id)
    def transfer(self):
        self.root.destroy()
        obj2=Transfer.transfer_class(self.id)
    def mini(self):
        self.root.destroy()
        obj2=Mini_Statement.mini_statement_class(self.id)
    def edit_profile(self):
        self.root.destroy()
        obj2=Edit_Profile.edit_profile_class(self.id)
    def edit_password(self):
        self.root.destroy()
        obj2=Edit_Password.edit_password_class(self.id)
    def edit_security(self):
        self.root.destroy()
        obj2=Edit_Security_Setting.edit_security_setting_class(self.id)
    def logout(self):
        self.root.destroy()
        obj2=Login.Login_class1()
    def search(self):
        self.root.destroy()
        Search.search_class(self.id)
    def about(self):
        self.root.destroy()
        obj2=aboutus.about_us(self.id)
#obj=Main("aa@gmail.com")