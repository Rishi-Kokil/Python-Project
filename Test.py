from tkinter import *
import WelcomeScreen
import DatabaseConnection

DatabaseConnection.Connection()  # Used for initial Database Setup
WelcomeScreen.WelcomeScreen(12)
