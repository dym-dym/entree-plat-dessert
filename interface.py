import tkinter
import customtkinter as ctk
# from utils.py import *

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# create CTk window 
app = ctk.CTk()
app.geometry("950x680")
app.title('Projet HAI902I: Aide à la décision')

#Create an input
Input = ctk.CTkEntry(app, width=250, height=30, placeholder_text="Enter a number of students or schools")
Input.pack()

# Use CTkButton 
def click_handler():
    print(f"Getting {Input.get()} schools and students")

button = ctk.CTkButton(master=app, text="Get matching", command=click_handler,
                       fg_color="transparent", border_width=2, border_color='#15869d')
button.place(relx=0.5, rely=0.15, anchor=ctk.CENTER)

# Make a title in the page
title = ctk.CTkLabel(app, text='Mariage stable entre étudiants et établissements')
title.pack(padx=5, pady=10)

#Create frames in the app
frame1 = ctk.CTkFrame(master=app)


#run the app
app.mainloop()