
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import Constants
import mysql.connector
import DatabaseConnection
import HomeScreen
import datetime
from tkinter import messagebox


class RegistrationScreen:
    obj1 = DatabaseConnection.Connection()

    def getData(self , root1 , root2):
        dict1 = {"A+ve" : "A_positive", "A-ve": "A_negative", "B+ve": "B_positive", "B-ve": "B_negative", "AB+ve": "AB_positive","AB-ve": "AB_negative","O+ve": "O_positive","O-ve": "O_negative"}

        address = self.address_text.get("1.0", END).replace('\n', " ")

        stripped_address = address.strip()

        self.unique_id = "VBC" + str(self.row_count) + str(datetime.date.today())
        self.sqlQuery = strQuery = f'''INSERT INTO REGISTRATION VALUES ("{(self.unique_id)}","{self.name.get()}","{self.gender.get()}",'{self.date_of_birth.get()}',"{self.phone.get()}","{self.email.get()}","{stripped_address}","{self.govt_id_type.get()}","{self.govt_id_number.get()}",'{datetime.date.today() }',"{dict1[self.blood_group.get()] }"); '''
        flag = False

        try:
            self.mycursor.execute(self.sqlQuery)
            self.mydb.commit()
            flag = True

        except Exception as e:
            flag = False
            print("An exception occurred: ", e)

        if(flag):
            self.mydb.close()
            title = "Successful"
            message = "Your Data has been stored int the Database"
            messagebox.showinfo(title, message)
            root1.destroy()
            root2.HomeScreen()

        else:
            print('Query Not Executed')

        print("Registration:- ",self.mydb.is_connected())

    def backButton(self , root1 , root2):
        root1.destroy()
        root2.HomeScreen()

    def __init__(self):

        # --------------------------------DatabaseConnection For storing and retriving Data---------------
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="tiger")
        self.mycursor = self.mydb.cursor()
        print(self.mydb)
        self.mycursor.execute("USE BLOODBANK")
        # getting no of rows in registration table
        self.mycursor.execute("SELECT * FROM REGISTRATION;")
        resultSet = self.mycursor.fetchall()    #returns List of Tuples

        self.row_count = len(resultSet)
        # ----------------------------------------------------------------------------------------------
        self.registrationScreen = Tk()
        self.registrationScreen.title("Registration Screen")
        self.registrationScreen.geometry("1000x700")
        self.registrationScreen.config(bg=Constants.Constants.secondaryColor)
        self.registrationScreen.wm_attributes('-fullscreen', True)

        # ----------------Variables=================

        self.name = StringVar()
        self.date_of_birth = StringVar()
        self.gender = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.address = ""
        self.govt_id_type = StringVar()
        self.govt_id_number = StringVar()
        self.blood_group = StringVar()

        self.unique_id = ""
        self.sqlQuery = ""

        # ---------------------------------

        self.title = Label(self.registrationScreen, text="Registration Form", font=(Constants.Constants.titleFont, 25),background=Constants.Constants.frameBackground )
        self.title.place(relx=0, rely=0, relwidth=1 , relheight= 0.09)

        photo = tk.PhotoImage(file="left_arrow.png").subsample(11, 11)
        Button(self.registrationScreen, text='back', image=photo, anchor="center",
               background=Constants.Constants.frameBackground, relief=FLAT,
               command=lambda: self.backButton(self.registrationScreen, HomeScreen)).place(relx=0.01, rely=0.01,
                                                                                           relheight=0.08)


        ttk.Style().configure("pad.TEntry", padding="1 1 1 1")

        self.personal_info = LabelFrame(self.registrationScreen, text="Personal Info", background=Constants.Constants.frameBackground,foreground=Constants.Constants.frameForeground,font=(Constants.Constants.titleFont, 15), relief=FLAT ,labelanchor= "nw" )
        self.personal_info.place(relx=0.01, rely=0.1, relwidth = 0.98, relheight=0.5)


        self.labelname = Label(self.personal_info, text="Name", font=(Constants.Constants.subTitleFont, 15),background=Constants.Constants.frameBackground)
        self.labelname.place(relx=0.001, rely=0.1 , relwidth= 0.1)

        self.name = ttk.Entry(self.personal_info, font=(Constants.Constants.subTitleFont, 15), style="pad.TEntry",
                              textvariable=self.name)
        self.name.focus_force()
        self.name.place(relx=0.15, rely=0.1, relwidth=0.4)

        self.labelgender = Label(self.personal_info, text="Gender", font=(Constants.Constants.subTitleFont, 15),background=Constants.Constants.frameBackground)
        self.labelgender.place(relx=0.57, rely=0.1, relwidth=0.1)

        self.combo_box_gender = ttk.Combobox(self.personal_info, font=(Constants.Constants.subTitleFont, 15),
                                      textvariable=self.gender)
        self.combo_box_gender["value"] = (
        "Select Option", "Male", "Female", "Other")
        self.combo_box_gender.current(0)
        self.combo_box_gender.place(relx=0.7, rely=0.1, relwidth=0.2)

        self.labelphone = Label(self.personal_info, text="Phone", font=(Constants.Constants.subTitleFont, 15),
                               background=Constants.Constants.frameBackground)
        self.labelphone.place(relx=0.001, rely=0.3, relwidth=0.1)

        self.phone = ttk.Entry(self.personal_info, font=(Constants.Constants.subTitleFont, 15), style="pad.TEntry",
                              textvariable=self.phone)
        self.phone.place(relx=0.15, rely=0.3, relwidth=0.2)

        self.labelemail = Label(self.personal_info, text="Email", font=(Constants.Constants.subTitleFont, 15),
                                background=Constants.Constants.frameBackground)
        self.labelemail.place(relx=0.4, rely=0.3, relwidth=0.1)

        self.email = ttk.Entry(self.personal_info, font=(Constants.Constants.subTitleFont, 15), style="pad.TEntry",
                               textvariable=self.email)
        self.email.place(relx=0.52, rely=0.3, relwidth=0.2)

        self.labeldate = Label(self.personal_info, text="Date Of Birth", font=(Constants.Constants.subTitleFont, 15),
                                background=Constants.Constants.frameBackground)
        self.labeldate.place(relx=0.67, rely=0.3, relwidth=0.15)

        self.date = ttk.Entry(self.personal_info, font=(Constants.Constants.subTitleFont, 15), style="pad.TEntry",
                               textvariable=self.date_of_birth)
        self.date.place(relx=0.8, rely=0.3, relwidth=0.18)

        self.labeladdress = Label(self.personal_info, text="Address", font=(Constants.Constants.subTitleFont, 15),
                               background=Constants.Constants.frameBackground)
        self.labeladdress.place(relx=0.001, rely=0.5, relwidth=0.1)

        self.address_text = tk.Text(self.personal_info ,font=(Constants.Constants.subTitleFont, 15))
        self.address_text.place(relx=0.15, rely=0.5, relwidth=0.4 , relheight= 0.35)

        # address = self.address.get()
        # ----------------------------Frame 2
        self.more_info = LabelFrame(self.registrationScreen, text="More Info",
                                        background=Constants.Constants.frameBackground,
                                        foreground=Constants.Constants.frameForeground,
                                        font=(Constants.Constants.titleFont, 15),relief=FLAT ,labelanchor="nw")
        self.more_info.place(relx=0.01, rely=0.61, relwidth=0.98, relheight=0.38)

        self.labelgovt_id_type = Label(self.more_info, text="Govt ID", font=(Constants.Constants.subTitleFont, 15),
                               background=Constants.Constants.frameBackground)
        self.labelgovt_id_type.place(relx=0.001, rely=0.1, relwidth=0.1)

        # self.options = ["Select Option","Aadhar Card", "PAN Card", "Driving license","Voter ID","Passport"]
        self.combo_box = ttk.Combobox(self.more_info, font=(Constants.Constants.subTitleFont, 15),textvariable=self.govt_id_type)
        self.combo_box["value"] = ("Select Option","Aadhar Card", "PAN Card", "Driving license","Voter ID","Passport")
        self.combo_box.current(0)
        self.combo_box.place(relx=0.15, rely=0.1, relwidth=0.2)

        self.govt_id_number = ttk.Entry(self.more_info, font=(Constants.Constants.subTitleFont, 15), style="pad.TEntry",
                              textvariable=self.govt_id_number)
        self.govt_id_number.place(relx=0.4, rely=0.1, relwidth=0.15)

        self.labelbloodgroup = Label(self.more_info, text="Blood Group", font=(Constants.Constants.subTitleFont, 15),
                                background=Constants.Constants.frameBackground)
        self.labelbloodgroup.place(relx=0.001, rely=0.3, relwidth=0.1)

        self.combo_box_blood_group = ttk.Combobox(self.more_info, font=(Constants.Constants.subTitleFont, 15),
                                      textvariable=self.blood_group)
        self.combo_box_blood_group["value"] = ("Select Option", "A+ve", "A-ve", "B+ve", "B-ve", "AB+ve","AB-ve","O+ve","O-ve")
        self.combo_box_blood_group.current(0)
        self.combo_box_blood_group.place(relx=0.15, rely=0.3, relwidth=0.15)

        self.button1 = Button(self.more_info,
                              text='Submit',
                              font=(Constants.Constants.subTitleFont, 20),
                              bg=Constants.Constants.primaryColor,
                              fg=Constants.Constants.secondaryColor , command=lambda : self.getData(self.registrationScreen , HomeScreen))
        self.button1.place(relx=0.82, rely=0.78, relwidth=0.15 )


        self.registrationScreen.mainloop()
