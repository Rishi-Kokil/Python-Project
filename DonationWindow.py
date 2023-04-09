from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import Constants
import mysql.connector
import HomeScreen
import datetime


class DonationScreen:

    def donationButtonClick(self , root1 , root2):
        self.mycursor.execute("SELECT * FROM DONATION;")
        resultSet = self.mycursor.fetchall()

        self.row_count = len(resultSet)
        self.donation_id = "ID"+str(self.row_count)+str(datetime.date.today())

        self.sqlQuery = f'''INSERT INTO DONATION VALUES('{self.donation_id}','{self.reg_id}' , '{self.name}','{self.blood_group}' , '{datetime.date.today()}');'''
        flag = False

        self.sqlQuery2 = f'''UPDATE BLOOD_BANK SET {self.blood_group}_UNITS = {self.blood_group}_UNITS + 1 ;'''

        print(self.sqlQuery)
        print(self.sqlQuery2)
        try:
            self.mycursor.execute(self.sqlQuery)
            self.mydb.commit()
            self.mycursor.execute(self.sqlQuery2)
            self.mydb.commit()
            flag = True

        except Exception as e:
            flag = False
            print("An exception occurred: ", e)

        if (flag):
            self.mydb.close()
            root1.destroy()
            root2.HomeScreen()
        else:
            print('Query Not Executed')

        print("Registration:- ", self.mydb.is_connected())


    def getData(self):
        self.sname = "VBC02023-04-09"
        # sqlQuery = f"SELECT * FROM REGISTRATION WHERE REGISTRATION_ID = '{self.searchname.get()}';"
        sqlQuery = f"SELECT * FROM REGISTRATION WHERE REGISTRATION_ID = '{self.sname}';"
        print(sqlQuery)
        self.mycursor.execute(sqlQuery)
        resultSet = self.mycursor.fetchall()

        if(len(resultSet) == 0):
            print('No user')

        else:
            for data in resultSet:
                print('entered else')
                self.userFrame = Frame(self.donationScreen, bg=Constants.Constants.frameBackground)
                self.userFrame.place(relx=0.01, rely=0.15, relwidth=0.98, relheight=0.2)
                self.reg_id = data[0]
                self.name = data[1]
                self.phone = data[4]
                self.email = data[5]
                self.blood_group = data[10]
                print(self.name, self.phone, self.reg_id, self.email, self.blood_group)

                Labelreg_id = Label(self.userFrame, text="ID : "+ self.reg_id, font=(Constants.Constants.titleColor, 25),
                                    background=Constants.Constants.frameBackground)
                Labelreg_id.place(relx=0.05, rely=0.01)

                Labelname = Label(self.userFrame, text="Name : "+self.name, font=(Constants.Constants.subTitleColor, 14),
                                  background=Constants.Constants.frameBackground,
                                  fg='black')
                Labelname.place(relx=0.05, rely=0.25)

                Labelblood_group = Label(self.userFrame, text='Blood Group : '+self.blood_group,
                                         font=(Constants.Constants.subSubTitleColor, 11),
                                         background=Constants.Constants.frameBackground)
                Labelblood_group.place(relx=0.05, rely=0.55)

                Labelblood_phone = Label(self.userFrame, text='Phone : '+self.phone,
                                         font=(Constants.Constants.subSubTitleColor, 11),
                                         background=Constants.Constants.frameBackground)
                Labelblood_phone.place(relx=0.18, rely=0.55)

                Labelemail = Label(self.userFrame, text="Email : "+self.email,
                                   font=(Constants.Constants.subSubTitleColor, 11),
                                   background=Constants.Constants.frameBackground)
                Labelemail.place(relx=0.28, rely=0.55)

                self.donateButton = Button(self.userFrame,
                                      text='Donate Blood',
                                      font=(Constants.Constants.subTitleFont, 20),
                                      bg=Constants.Constants.primaryColor,
                                      fg=Constants.Constants.secondaryColor,
                                      command=lambda: self.donationButtonClick(self.donationScreen , HomeScreen))
                self.donateButton.place(relwidth= 0.2 , relheight= 0.25 , relx= 0.73 , rely=0.4)


    def __init__(self):
        # ---------------------------------------DatabseConnection For Donating Blood------------------
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="tiger")
        self.mycursor = self.mydb.cursor()
        print(self.mydb)
        self.mycursor.execute("USE BLOODBANK")
        # --------------------------------------------------------------------------------------
        self.donationScreen = Tk()
        self.donationScreen.title("Registration Screen")
        self.donationScreen.geometry("1000x700")
        self.donationScreen.config(bg=Constants.Constants.secondaryColor)
        self.donationScreen.wm_attributes('-fullscreen', True)

        # -------------------Variables
        self.searchname = StringVar()


        self.reg_id = ""
        self.name = ""
        self.blood_group = ""
        self.phone = ""
        self.email = ""

        # ------------------------

        self.searchBar = LabelFrame(self.donationScreen,
                                    background=Constants.Constants.frameBackground,
                                    foreground=Constants.Constants.frameForeground,
                                    font=(Constants.Constants.titleFont, 15), relief=FLAT, labelanchor="nw")
        self.searchBar.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)

        self.sname = Entry(self.searchBar, font=(Constants.Constants.subTitleFont, 18),  background= Constants.Constants.secondaryColor,
                              textvariable=self.searchname)
        self.sname.focus_force()
        self.sname.place(relx=0.1, rely=0.27, relwidth=0.6 )

        self.button1 = Button(self.searchBar,
                              text='Search',
                              font=(Constants.Constants.subTitleFont, 20),
                              bg=Constants.Constants.primaryColor,
                              fg=Constants.Constants.secondaryColor,
                              command=lambda: self.getData())
        self.button1.place(relx=0.75, rely=0.15, relwidth=0.13)


        self.donationScreen.mainloop()


# ibj = DonationScreen()