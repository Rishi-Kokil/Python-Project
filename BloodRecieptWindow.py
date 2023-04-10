from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
import Constants
import mysql.connector
import HomeScreen
import datetime


class BloodReceiptScreen:

    def requestButtonClick(self, root1 , root2):
        dict1 = {"A+ve" : "A_positive", "A-ve": "A_negative", "B+ve": "B_positive", "B-ve": "B_negative", "AB+ve": "AB_positive","AB-ve": "AB_negative","O+ve": "O_positive","O-ve": "O_negative"}

        self.mycursor.execute(f"SELECT {dict1[self.req_bloodgroup.get()]}_UNITS FROM BLOOD_BANK;")
        resultset = self.mycursor.fetchall()

        print(resultset[0][0])
        countQty = int(resultset[0][0])
        self.mydb.commit()

        if(self.req_bloodQty.get() <= countQty):
            self.mycursor.execute("SELECT * FROM DONATION;")
            resultSet = self.mycursor.fetchall()

            self.row_count = len(resultSet)
            self.donation_id = "ID" + str(self.row_count) + str(datetime.date.today())

            self.sqlQuery = f'''INSERT INTO BLOODRECIPIENT VALUES('{self.donation_id}','{self.reg_id}' , '{self.name}','{self.blood_group}' , '{datetime.date.today()}','{dict1[self.req_bloodgroup.get()]}',{self.req_bloodQty.get()});'''
            flag = False

            self.sqlQuery2 = f'''UPDATE BLOOD_BANK SET {self.blood_group}_UNITS = {self.blood_group}_UNITS - {self.req_bloodQty.get()} ;'''

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
                messagebox.showinfo("SuccessFull","The Entry has been made in the database")
                self.mydb.close()
                root1.destroy()
                root2.HomeScreen()
            else:
                print('Query Not Executed')

            print("blood Recipt:- ", self.mydb.is_connected())

        else:
            title = "Error in Execution"
            message = "Quantity you entered exceeds the current value present"
            messagebox.showerror(title, message)

    def bloodReciptButton(self):
        self.donateButton.destroy()
        self.requestFrame = Frame(self.bloodReceiptWindow, bg=Constants.Constants.frameBackground)
        self.requestFrame.place(relx=0.01, rely=0.56, relwidth=0.98, relheight=0.15)
        self.req_bloodgroup = StringVar()
        self.req_bloodQty = IntVar()


        Labelreq_blood_group = Label(self.requestFrame, text="Blood_Group" , font=(Constants.Constants.titleColor, 14),
                            background=Constants.Constants.frameBackground)
        Labelreq_blood_group.place(relx=0.05, rely=0.3)

        self.combo_box_blood_group = ttk.Combobox(self.requestFrame, font=(Constants.Constants.subTitleFont, 13),
                                                  textvariable=self.req_bloodgroup)
        self.combo_box_blood_group["value"] = (
        "Select Option", "A+ve", "A-ve", "B+ve", "B-ve", "AB+ve", "AB-ve", "O+ve", "O-ve")
        self.combo_box_blood_group.current(0)
        self.combo_box_blood_group.place(relx=0.25, rely=0.3, relwidth=0.15)


        Labelqty = Label(self.requestFrame, text="Quanitity", font=(Constants.Constants.subTitleColor, 14),
                          background=Constants.Constants.frameBackground,
                          fg='black')
        Labelqty.place(relx=0.05, rely=0.6)

        self.entryQty = ttk.Entry(self.requestFrame, font=(Constants.Constants.subTitleFont, 13), style="pad.TEntry",
                                        textvariable=self.req_bloodQty)
        self.entryQty.place(relx=0.25, rely=0.6, relwidth=0.15)

        self.requestButton = Button(self.requestFrame,
                                   text='Request',
                                   font=(Constants.Constants.subTitleFont, 20),
                                   bg=Constants.Constants.primaryColor,
                                   fg=Constants.Constants.secondaryColor,
                                   command=lambda: self.requestButtonClick(self.bloodReceiptWindow, HomeScreen))
        self.requestButton.place(relwidth=0.2, relheight=0.25, relx=0.73, rely=0.4)



    def getData(self):
        # self.sname = "VBC02023-04-10"
        sqlQuery = f"SELECT * FROM REGISTRATION WHERE REGISTRATION_ID = '{self.searchname.get()}';"
        # sqlQuery = f"SELECT * FROM REGISTRATION WHERE REGISTRATION_ID = '{self.sname}';"
        print(sqlQuery)
        self.mycursor.execute(sqlQuery)
        resultSet = self.mycursor.fetchall()

        if(len(resultSet) == 0):
            print('No user')

        else:
            for data in resultSet:
                print('entered else')
                self.userFrame = Frame(self.bloodReceiptWindow, bg=Constants.Constants.frameBackground)
                self.userFrame.place(relx=0.01, rely=0.33, relwidth=0.98, relheight=0.2)
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
                                      text='Request',
                                      font=(Constants.Constants.subTitleFont, 20),
                                      bg=Constants.Constants.primaryColor,
                                      fg=Constants.Constants.secondaryColor,
                                      command=lambda: self.bloodReciptButton())
                self.donateButton.place(relwidth= 0.2 , relheight= 0.25 , relx= 0.73 , rely=0.4)



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
        self.bloodReceiptWindow = Tk()
        self.bloodReceiptWindow.title("Blood Receipt")
        self.bloodReceiptWindow.geometry("1000x700")
        self.bloodReceiptWindow.config(bg=Constants.Constants.secondaryColor)
        self.bloodReceiptWindow.wm_attributes('-fullscreen', True)

        # -----------------------------------------------------------------------------------
        self.searchname = StringVar()

        self.reg_id = ""
        self.name = ""
        self.blood_group = ""
        self.phone = ""
        self.email = ""
        # ----------------------------------------------------------------------------------------------

        self.titleLabel = Label(self.bloodReceiptWindow,
                                text="Blood Receipt",
                                font=(Constants.Constants.titleFont, 35, "bold"),
                                padx=10,
                                pady=5,
                                bg=Constants.Constants.secondaryColor, anchor='center'
                                )
        self.titleLabel.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.15)

        photo = tk.PhotoImage(file="BackButton.png").subsample(6, 6)

        photo = tk.PhotoImage(file="BackButton.png").subsample(6, 6)
        Button(self.bloodReceiptWindow, text='back', image=photo, anchor="center",
               background=Constants.Constants.secondaryColor, relief=FLAT,
               command=lambda: self.backButton(self.bloodReceiptWindow, HomeScreen)).place(relx=0.01, rely=0.01,
                                                                                    relheight=0.08)

        self.searchBar = LabelFrame(self.bloodReceiptWindow,
                                    background=Constants.Constants.frameBackground,
                                    foreground=Constants.Constants.frameForeground,
                                    font=(Constants.Constants.titleFont, 15), relief=FLAT, labelanchor="nw")
        self.searchBar.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.1)

        self.sname = Entry(self.searchBar, font=(Constants.Constants.subTitleFont, 18),
                           background=Constants.Constants.secondaryColor,
                           textvariable=self.searchname)
        self.sname.focus_force()
        self.sname.place(relx=0.1, rely=0.27, relwidth=0.6)

        self.button1 = Button(self.searchBar,
                              text='Search',
                              font=(Constants.Constants.subTitleFont, 20),
                              bg=Constants.Constants.primaryColor,
                              fg=Constants.Constants.secondaryColor,
                              command=lambda: self.getData())
        self.button1.place(relx=0.75, rely=0.15, relwidth=0.13)


        self.bloodReceiptWindow.mainloop()


# obj = BloodReceiptScreen()
