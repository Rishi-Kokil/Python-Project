import tkinter as tk
from tkinter import *
import Constants
import RegistrationWindow
import LoginScreen
import DonationWindow

class HomeScreen:
    def _registration(self , root1 , root2):
        root1.destroy()
        root2.RegistrationScreen()
    def _donation(self , root1 , root2):
        root1.destroy()
        root2.DonationScreen()

    def backButton(self , root1 , root2):
        root1.destroy()
        root2.LoginScreen()

    def __init__(self):

        self.homeScreen = Tk()
        self.homeScreen.geometry("1000x700")
        self.homeScreen.title("HomeScreen")
        self.homeScreen.config(bg = Constants.Constants.secondaryColor)
        self.homeScreen.attributes('-fullscreen', True)



        photo = tk.PhotoImage(file="left_arrow.png").subsample(9, 9)
        Button(self.homeScreen, text='back', image=photo, anchor="center",
               background=Constants.Constants.secondaryColor, relief=FLAT,
               command=lambda: self.backButton(self.homeScreen, LoginScreen)).place(relx=0.01, rely=0.01,
                                                                                           relheight=0.08)

        self.titleLabel = Label(self.homeScreen,
                                text="Home",
                                font=(Constants.Constants.titleFont, 30, "bold"),
                                padx=10,
                                pady=5,
                                bg=Constants.Constants.secondaryColor,anchor='center'
                                )
        self.titleLabel.place(relx=0.3, rely=0, relwidth=0.4, relheight=0.15)

        self.registerButton = Button(self.homeScreen,
                              text='Register User',
                              font=(Constants.Constants.subTitleFont, 20),
                              bg=Constants.Constants.primaryColor,
                              fg=Constants.Constants.secondaryColor,
                              command=lambda: self._registration(self.homeScreen , RegistrationWindow))
        self.registerButton.place(relx=0.22, rely=0.4, relwidth=0.25 , relheight=0.15)

        self.DonateBloodButton = Button(self.homeScreen,
                              text='Donate Blood',
                              font=(Constants.Constants.subTitleFont, 20),
                              bg=Constants.Constants.primaryColor,
                              fg=Constants.Constants.secondaryColor,
                              command=lambda: self._donation(self.homeScreen , DonationWindow))
        self.DonateBloodButton.place(relx=0.53, rely=0.4, relwidth=0.25 , relheight=0.15 )
        self.Blood_Availability = Button(self.homeScreen,
                              text='Blood Availability',
                              font=(Constants.Constants.subTitleFont, 20),
                              bg=Constants.Constants.primaryColor,
                              fg=Constants.Constants.secondaryColor,
                              command=lambda: self._checkUserNamePassword(username.get(), password.get(),
                                                                          self.loginscreen, HomeScreen))
        self.Blood_Availability.place(relx=0.22, rely=0.65, relwidth=0.25 , relheight=0.15)

        self.GiveBlood = Button(self.homeScreen,
                              text='Recieve Blood',
                              font=(Constants.Constants.subTitleFont, 20),
                              bg=Constants.Constants.primaryColor,
                              fg=Constants.Constants.secondaryColor,
                              command=lambda: self._checkUserNamePassword(username.get(), password.get(),
                                                                          self.loginscreen, HomeScreen))
        self.GiveBlood.place(relx=0.53, rely=0.65, relwidth=0.25 , relheight=0.15)



        self.homeScreen.mainloop()

