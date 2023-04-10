import tkinter
from tkinter import *
import tkinter.ttk as ttk
import Constants
import mysql.connector
import HomeScreen
from tkinter import messagebox

class LoginScreen:
    def _checkUserNamePassword(self , root1 , root2):
        flag = False
        self.mycursor.execute("SELECT * FROM USERS;")
        resultSet = self.mycursor.fetchall()    #returns List of Tuples
        for element in resultSet:
            if(element[0] == self.username.get() and element[1]== self.password.get()):
                flag = True

        if(flag):
            self.mydb.close()
            print('Login :- ', self.mydb.is_connected())
            root1.destroy()
            root2.HomeScreen()
        else:
            title = "Error while Logging In"
            text = "Invalid Unsername Or Password"
            messagebox.showinfo(title , text)


    def __init__(self):
        # ----------------------------------------Re Establishing Connection with the database for Login
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="tiger")
        self.mycursor = self.mydb.cursor()
        print('Login :- ',self.mydb.is_connected())
        self.mycursor.execute("USE BLOODBANK")
        # ------------------------------------------
        self.loginscreen = Tk()
        self.loginscreen.title('Login')
        self.loginscreen.geometry('1000x700')
        self.loginscreen.config(bg = Constants.Constants.secondaryColor)
        self.loginscreen.wm_attributes('-fullscreen', True)

        self.username = StringVar()
        self.password = StringVar()

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

        ttk.Style().configure("pad.TEntry", padding="5 5 5 5")

        self.unameEntry = ttk.Entry(self.frame2 , font=(Constants.Constants.subTitleFont , 15),  style="pad.TEntry" ,textvariable= self.username)
        self.unameEntry.focus_force()
        self.unameEntry.place(relx=0.1, rely=0.25, relwidth=0.80)

        self.password = Label(self.frame2, text="Password", font=(Constants.Constants.subTitleFont, 15),
                              bg=Constants.Constants.secondaryColor)
        self.password.place(relx=0.1, rely=0.35)

        self.password = ttk.Entry(self.frame2 , font=(Constants.Constants.subTitleFont , 15),show="*"  ,style="pad.TEntry" , textvariable= self.password,)
        self.password.place(relx=0.1 , rely=0.4 , relwidth= 0.80)

        self.button1 = Button(self.frame2,
                              text='Login',
                              font=(Constants.Constants.subTitleFont, 20),
                              bg=Constants.Constants.primaryColor,
                              fg=Constants.Constants.secondaryColor,
                              command=lambda: self._checkUserNamePassword(self.loginscreen , HomeScreen))

        self.button1.place(relx=0.25, rely=0.55, relwidth=0.5)

        # ---------------------------------------
        self.loginscreen.mainloop()


