import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from utils import *
from test_output import *
from matching import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Projet HAI902I: Aide à la décision')
        self.geometry("1280x720")
        self.grid_columnconfigure((0, 1), weight=1)

        def click_handler():
            input_value = self.Input.get()

            try:
                input_value = int(input_value)  # Convert input to integer (assuming it's a number)
                result_file = "matching_results.txt"
                random_test(input_value, input_value, result_file)  # Use the input as both student_number and school_number

                # Read the results from the file
                with open(result_file, "r") as file:
                    result_text = file.read()

                # Update the output label
                self.output_label.configure(text=result_text)

            except ValueError:
                print("Invalid input. Please enter a valid number.")


        # Make a title in the page
        self.title = ctk.CTkLabel(self, text="Voici une implémentation de l'algorithme de mariage stable entre étudiants et établissements."+'\n'+" Veuillez rentrer une valeur correspondant aux nombre d'étudiants et d'écoles que vous souhaitez mettre en relation :")
        self.title.grid(row=0, padx=5, pady=10)

        # Create an input
        self.Input = ctk.CTkEntry(self, width=250, height=30, placeholder_text="Enter a number of students or schools")
        self.Input.grid(row=1, padx=5, pady=10, sticky="ew")

        # Create a CTk Button
        self.button = ctk.CTkButton(
            master=self, text="Get matching", command=click_handler,
            fg_color="transparent", border_width=2, border_color='#15869d'
        )
        self.button.grid(row=2, padx=5, pady=10, sticky="ew")

        # Create a scrollable frame for displaying the result
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=30)
        self.scroll_frame.grid(row=3, padx=5, pady=10, sticky="ew")

        # Create a label for displaying the result within the scroll frame
        self.output_label = ctk.CTkLabel(self.scroll_frame, text='', justify='left')
        self.output_label.pack(fill='both', expand=True)

        # Placeholder for students and schools (you need to define these variables)
        self.students = np.array([])
        self.schools = np.array([])

if __name__ == "__main__":
    app = App()
    app.mainloop()