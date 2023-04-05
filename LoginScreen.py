import tkinter
from tkinter import *
import tkinter.ttk as ttk
import Constants
import mysql.connector
import DatabaseConnection
import HomeScreen

class LoginScreen:

    def _checkUserNamePassword(self , uname , passwd , root1 , root2):
        obj = DatabaseConnection.Connection()
        result = obj.checkUsernamePassword(uname , passwd)
        if(result == True):
            root1.destroy()
            root2.HomeScreen()

        else:
            print("Not SuccessFull")

    def __init__(self):
        self.name = "LoginScreen"
        self.loginscreen = Tk()
        self.loginscreen.title('Login')
        self.loginscreen.geometry('1000x700')
        self.loginscreen.config(bg = Constants.Constants.secondaryColor)

        username = StringVar()
        password = StringVar()

        self.frame1 = Frame(self.loginscreen, bg = Constants.Constants.primaryColor)
        self.frame1.place(relx=0, rely=0, relwidth=0.5, relheight=1)


        self.frame2 = Frame(self.loginscreen , bg=Constants.Constants.secondaryColor)
        self.frame2.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

        #Frame 1 Labels --------------------------

        self.labelSlogan = Label(self.frame1,
                            text="Once a blood donor,\nalways a lifesaver.",
                            font=(Constants.Constants.titleFont , 35),
                            bg=Constants.Constants.primaryColor,
                            fg=Constants.Constants.secondaryColor)
        self.labelSlogan.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Frame 2 Labels --------------------------

        self.labelUsername = Label(self.frame2,text="Username",font=(Constants.Constants.subTitleFont, 15),bg=Constants.Constants.secondaryColor)
        self.labelUsername.place(relx=0.1 , rely=0.2)

        ttk.Style().configure("pad.TEntry" , padding = "5 5 5 5")

        self.unameEntry = ttk.Entry(self.frame2 , font=(Constants.Constants.subTitleFont , 15),  style="pad.TEntry" ,textvariable= username)
        self.unameEntry.focus_force()
        self.unameEntry.place(relx=0.1, rely=0.25, relwidth=0.80)


        self.password = ttk.Entry(self.frame2 , font=(Constants.Constants.subTitleFont , 15),show="*"  ,style="pad.TEntry" , textvariable= password,)
        self.password.place(relx=0.1 , rely=0.4 , relwidth= 0.80)

        self.password = Label(self.frame2,text="Password",font=(Constants.Constants.subTitleFont, 15),bg=Constants.Constants.secondaryColor)
        self.password.place(relx=0.1 , rely=0.35)

        self.button1 = Button(self.frame2,
                              text='Login',
                              font=(Constants.Constants.subTitleFont, 20),
                              bg=Constants.Constants.primaryColor,
                              fg=Constants.Constants.secondaryColor,
                              command=lambda: self._checkUserNamePassword(username.get() , password.get() ,self.loginscreen , HomeScreen))
        self.button1.place(relx=0.25, rely=0.55, relwidth=0.5)

        # ---------------------------------------
        self.loginscreen.mainloop()


# obj = LoginScreen()