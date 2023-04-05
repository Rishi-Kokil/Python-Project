import tkinter
from tkinter import *
import LoginScreen
import Constants

class WelcomeScreen:

    def _on_click(self , root1 , root2):
        root1.destroy()
        root2.LoginScreen()

    def __init__(self, x):
        self.x = x
        self.welcomeScreen = Tk()
        self.welcomeScreen.title('VESIT Blood Donation Centre')
        self.welcomeScreen.geometry('1000x700')
        self.welcomeScreen.config(bg = Constants.Constants.secondaryColor)

        self.titleLabel = Label(self.welcomeScreen,
                           text="VESIT \n Blood Donation Centre",
                           font=(Constants.Constants.titleFont, 30, "bold"),
                           padx=10,
                           pady=5,
                            bg=Constants.Constants.secondaryColor
                           )
        self.titleLabel.place(relx=0, rely=0, relwidth=1, relheight=0.25)

        self.button1 = Button(self.welcomeScreen,
                         text='Get Started',
                         font=(Constants.Constants.subTitleFont, 20),
                         bg=Constants.Constants.primaryColor,
                         fg=Constants.Constants.secondaryColor,
                         command= lambda: self._on_click(self.welcomeScreen , LoginScreen))
        self.button1.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5)

        self.welcomeScreen.mainloop()



