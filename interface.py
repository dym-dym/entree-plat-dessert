import tkinter
import customtkinter as ctk
# from utils import *
# from test import * 

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#Create the CTk window 
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Projet HAI902I: Aide à la décision')
        self.geometry("1280x720")
        self.grid_columnconfigure((0, 1), weight=1)

        def click_handler():
            print(f"Getting {Input.get()} schools and students")

        #Create a CTk Button
        self.button = ctk.CTkButton(master=self, text="Get matching", command=click_handler,
                       fg_color="transparent", border_width=2, border_color='#15869d')
        self.button.place(relx=0.25, rely=0.25, anchor=ctk.CENTER)

        #Create CTk checkboxes
        self.checkbox_1 = ctk.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        self.checkbox_2 = ctk.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

        #Create an input
        self.Input = ctk.CTkEntry(self, width=250, height=30, placeholder_text="Enter a number of students or schools")
        self.Input.grid(row=2, padx=5, pady=10, sticky ="ew")

        #Display text
        self.text1 = ctk.CTkLabel(self, text='Mariage stable entre étudiants et établissements')
        self.text1.grid(row=3, padx=5, pady=10, sticky ="ew")
    
app = App()
#Create frames in the app
#frame1 = ctk.CTkFrame(master=app,
#                         height= app.winfo_height()*0.33,
#                         width = app.winfo_width()*0.33,
#                         fg_color="white")
#frame1.place(relx=0.33, rely=0.025)


#Run the app
app.mainloop()
