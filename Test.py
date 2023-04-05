from tkinter import *
import WelcomeScreen
WelcomeScreen.WelcomeScreen(12)


# import tkinter as tk
# from tkinter import *
#
# # Create a Tkinter window
# window = Tk()
# window.title("Blood Donation Registration Form")
#
# # Create labels for each field
# name_label = tk.Label(window, text="Name")
# dob_label = tk.Label(window, text="Date of Birth (YYYY-MM-DD)")
# gender_label = tk.Label(window, text="Gender")
# phone_label = tk.Label(window, text="Phone")
# email_label = tk.Label(window, text="Email")
# address_label = tk.Label(window, text="House Address")
# blood_group_label = tk.Label(window, text="Blood Group")
# id_label = tk.Label(window, text="Government ID No.")
#
# # Create entry fields for each label
# name_entry = tk.Entry(window)
# dob_entry = tk.Entry(window)
# gender_entry = tk.Entry(window)
# phone_entry = tk.Entry(window)
# email_entry = tk.Entry(window)
# address_entry = tk.Entry(window)
# blood_group_entry = tk.Entry(window)
# id_entry = tk.Entry(window)
#
# # Positioning the labels and entry fields on the window
# name_label.grid(row=0, column=0, padx=10, pady=5)
# name_entry.grid(row=0, column=1, padx=10, pady=5)
#
# dob_label.grid(row=1, column=0, padx=10, pady=5)
# dob_entry.grid(row=1, column=1, padx=10, pady=5)
#
# gender_label.grid(row=2, column=0, padx=10, pady=5)
# gender_entry.grid(row=2, column=1, padx=10, pady=5)
#
# phone_label.grid(row=3, column=0, padx=10, pady=5)
# phone_entry.grid(row=3, column=1, padx=10, pady=5)
#
# email_label.grid(row=4, column=0, padx=10, pady=5)
# email_entry.grid(row=4, column=1, padx=10, pady=5)
#
# address_label.grid(row=5, column=0, padx=10, pady=5)
# address_entry.grid(row=5, column=1, padx=10, pady=5)
#
# blood_group_label.grid(row=6, column=0, padx=10, pady=5)
# blood_group_entry.grid(row=6, column=1, padx=10, pady=5)
#
# id_label.grid(row=7, column=0, padx=10, pady=5)
# id_entry.grid(row=7, column=1, padx=10, pady=5)
#
# # Create a function to retrieve the data entered by the user
# def submit_form():
#     name = name_entry.get()
#     dob = dob_entry.get()
#     gender = gender_entry.get()
#     phone = phone_entry.get()
#     email = email_entry.get()
#     address = address_entry.get()
#     blood_group = blood_group_entry.get()
#     id_no = id_entry.get()
#
#     # Print the data to the console for testing
#     print("Name: ", name)
#     print("Date of Birth: ", dob)
#     print("Gender: ", gender)
#     print("Phone: ", phone)
#     print("Email: ", email)
#     print("Address: ", address)
#     print("Blood Group: ", blood_group)
#     print("ID No.: ", id_no)
#
# # Create a submit button
# submit_button = tk.Button(window, text="Submit", command=submit_form)
# submit_button.grid(row=8, column=1, padx=10, pady=10, sticky="E")
#
# # Make the window responsive
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
# window.rowconfigure(2, weight=1)
# window.rowconfigure(3, weight=1)
# window.rowconfigure(4, weight=1)
# window.rowconfigure(5, weight=1)
# window.rowconfigure(6, weight=1)
# window.rowconfigure(7, weight=1)
# window.rowconfigure(8, weight=1)
#
# window.mainloop()

