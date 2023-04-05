import tkinter
from tkinter import *
import Constants
import RegistrationWindow


class HomeScreen:
    def _registration(self , root1 , root2):
        root1.destroy()
        root2.RegistrationScreen()

    def __init__(self):
        self.homeScreen = Tk()
        self.homeScreen.geometry("1000x700")
        self.homeScreen.title("HomeScreen")
        self.homeScreen.config(bg = Constants.Constants.secondaryColor)
        self.homeScreen.attributes('-fullscreen', True)


        self.titleLabel = Label(self.homeScreen,
                                text="Home",
                                font=(Constants.Constants.titleFont, 30, "bold"),
                                padx=10,
                                pady=5,
                                bg=Constants.Constants.secondaryColor
                                )
        self.titleLabel.place(relx=0, rely=0, relwidth=1, relheight=0.15)

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
                              command=lambda: self._checkUserNamePassword(username.get(), password.get(),
                                                                          self.loginscreen, HomeScreen))
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
