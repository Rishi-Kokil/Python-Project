from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
import Constants
import mysql.connector
import HomeScreen
import datetime
from tkinter import messagebox

class BloodAvailability:

    def labelCreator(self , text1 , text2 , x , y):
        print('Functioncall')
        return Label(self.bloodAvailabilityScreen , text= text1 + ' :\t'+ text2 ,
                     font=(Constants.Constants.subTitleFont, 12),padx=10,pady=5,bg=Constants.Constants.secondaryColor, anchor='center').place(relx=x , rely=y)


    def backButton(self, root1, root2):
        root1.destroy()
        root2.HomeScreen()

    def __init__(self):
        # ----------------------------Database Connection-------------------------------------------
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="tiger")
        self.mycursor = self.mydb.cursor()
        print(self.mydb)
        self.mycursor.execute("USE BLOODBANK")

        # -------------------------------------------------------------------------------------
        self.bloodAvailabilityScreen = Tk()
        self.bloodAvailabilityScreen.title("Blood Availability")
        self.bloodAvailabilityScreen.geometry("1000x700")
        self.bloodAvailabilityScreen.config(bg=Constants.Constants.secondaryColor)
        self.bloodAvailabilityScreen.wm_attributes('-fullscreen', True)

        self.titleLabel = Label(self.bloodAvailabilityScreen,
                                text="BloodBank Info",
                                font=(Constants.Constants.titleFont, 35, "bold"),
                                padx=10,
                                pady=5,
                                bg=Constants.Constants.secondaryColor, anchor='center'
                                )


        self.titleLabel.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.15)

        photo = tk.PhotoImage(file="BackButton.png").subsample(6, 6)

        photo = tk.PhotoImage(file="BackButton.png").subsample(6, 6)
        Button(self.bloodAvailabilityScreen, text='back', image=photo, anchor="center",
               background=Constants.Constants.secondaryColor, relief=FLAT,
               command=lambda: self.backButton(self.bloodAvailabilityScreen, HomeScreen)).place(relx=0.01, rely=0.01,
                                                                                           relheight=0.08)

        self.mycursor.execute('SELECT COUNT(REGISTRATION_ID) FROM REGISTRATION;')
        self.resultSet2 = self.mycursor.fetchall()
        self.tup2 = self.resultSet2[0]



        self.mycursor.execute('SELECT COUNT(DONATION_ID) FROM DONATION;')
        self.resultSet3 = self.mycursor.fetchall()
        self.tup3 = self.resultSet3[0]

        self.mycursor.execute('SELECT COUNT(RECIPIENT_ID) FROM BLOODRECIPIENT;')
        self.resultSet4 = self.mycursor.fetchall()
        self.tup4 = self.resultSet4[0]



        self.frameNumber1 = Frame(self.bloodAvailabilityScreen, bg = 'white' )
        self.frameNumber1.place(relx=0.05 , rely=0.2 , relwidth=0.3 , relheight=0.15)

        self.frameNumber2 = Frame(self.bloodAvailabilityScreen, bg = 'white' )
        self.frameNumber2.place(relx=0.35 , rely=0.2 , relwidth=0.3 , relheight=0.15)

        self.frameNumber3 = Frame(self.bloodAvailabilityScreen, bg = 'white' )
        self.frameNumber3.place(relx=0.65 , rely=0.2 , relwidth=0.3 , relheight=0.15)


        labelRegNUmber = Label(self.frameNumber1,
                         text=str(self.tup2[0]),
                         font=(Constants.Constants.titleFont, 20, "bold"),
                         padx=10,
                         pady=5,
                         bg=Constants.Constants.secondaryColor, anchor='center')
        labelRegNUmber.pack(side="top", fill="both", expand=True, padx=20, pady=0, anchor="center")

        labelReg = Label(self.frameNumber1,
                               text="Registrations",
                               font=(Constants.Constants.titleFont, 20, "bold"),
                               padx=10,
                               pady=5,
                               bg=Constants.Constants.secondaryColor, anchor='center')
        labelReg.pack(side="top", fill="both", expand=True, padx=20, pady=0, anchor="center")


        labelDonationNumber = Label(self.frameNumber2,
                         text=str(self.tup3[0]),
                         font=(Constants.Constants.titleFont, 20, "bold"),
                         padx=10,
                         pady=5,
                         bg=Constants.Constants.secondaryColor, anchor='center')
        labelDonationNumber.pack(side="top", fill="both", expand=True, padx=20, pady=0, anchor="center")

        labeldonate = Label(self.frameNumber2,
                         text="Blood Donations",
                         font=(Constants.Constants.titleFont, 20, "bold"),
                         padx=10,
                         pady=5,
                         bg=Constants.Constants.secondaryColor, anchor='center')
        labeldonate.pack(side="top", fill="both", expand=True, padx=20, pady=0, anchor="center")

        labelrecieptNUmber = Label(self.frameNumber3,
                                text=str(self.tup4[0]),
                                font=(Constants.Constants.titleFont, 20, "bold"),
                                padx=10,
                                pady=5,
                                bg=Constants.Constants.secondaryColor, anchor='center')

        labelrecieptNUmber.pack(side="top", fill="both", expand=True, padx=20, pady=0, anchor="center")

        labelrevieve = Label(self.frameNumber3,
                            text="Blood Provided",
                            font=(Constants.Constants.titleFont, 20, "bold"),
                            padx=10,
                            pady=5,
                            bg=Constants.Constants.secondaryColor, anchor='center')
        labelrevieve.pack(side="top", fill="both", expand=True, padx=20, pady=0, anchor="center")

        list1 = ["A Positive Units","B Positive Units","AB Positive Units","O Positive Units","A Negative Units","B Negative Units","O Negative Units","AB Negative Units",]
        self.mycursor.execute("SELECT * FROM BLOOD_BANK ;")
        self.resultSet1 = self.mycursor.fetchall()
        self.tup1 = self.resultSet1[0]

        x = 0.2
        y = 0.6
        index = 0
        count = 0
        for item in self.tup1:
            if (count == 4):
                x = 0.2
                y = 0.65
            self.labelCreator(list1[index],str(item),x,y)
            print(index)

            index = index + 1
            x = x + 0.15
            count = count + 1



        self.bloodAvailabilityScreen.mainloop()


# obj = BloodAvailability()