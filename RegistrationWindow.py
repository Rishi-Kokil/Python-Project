
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import Constants
import mysql.connector
import DatabaseConnection
import HomeScreen
import datetime



class RegistrationScreen:
    obj1 = DatabaseConnection.Connection()
    number = obj1.countingNoOfRows()

    def getData(self , root1 , root2):
        dict1 = {"A+ve" : "A_positive", "A-ve": "A_negative", "B+ve": "B_positive", "B-ve": "B_negative", "AB+ve": "AB_positive","AB-ve": "AB_negative","O+ve": "O_positive","O-ve": "O_negative"}
        address = self.address_text.get("1.0",END).replace('\n' , " ")
        date = f"DATE({self.date_of_birth.get()})"


        self.saveDataToDataBase(self.name.get() , date ,self.gender.get(),self.phone.get(),self.email.get(),address,self.govt_id_type.get(),self.govt_id_number.get(),dict1[self.blood_group.get()] ,root1,root2)

    print('Form Not Submitted')

    def saveDataToDataBase(self,  name , date_of_birth , gender , phone , email , address , govt_id_type , govt_id_number , blood_group , root1 , root2):

        # date_of_registration = datetime.date.today()
        # unique_id = "VBC" + str(RegistrationScreen.number) + str(date_of_registration.year)
        #
        # strQuery = f"INSERT INTO REGISTRATION VALUES ({unique_id},{name},{gender},{date_of_birth},{phone},{email},{address},{govt_id_type},{govt_id_number},{str(date_of_registration.year)},{blood_group}); "
        # print(strQuery)
        #
        # try:
        #     DatabaseConnection.Connection.mycursor.execute(strQuery)
        # except Exception as e:
        #     print("An error occurred:", e)
        #     return

        root1.destroy()
        root2.HomeScreen()


    def __init__(self):
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

        # ---------------------------------

        self.title = Label(self.registrationScreen, text="Registeration Form", font=(Constants.Constants.titleFont, 25),background=Constants.Constants.frameBackground )
        self.title.place(relx=0, rely=0, relwidth=1 , relheight= 0.09)


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

        self.gender = ttk.Entry(self.personal_info, font=(Constants.Constants.subTitleFont, 15), style="pad.TEntry",
                                textvariable=self.gender)
        self.gender.place(relx=0.7, rely=0.1, relwidth=0.2)

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


# obj = RegistrationScreen()