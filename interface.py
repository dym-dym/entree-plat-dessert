import tkinter as tk
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

        # Create an input
        self.Input = ctk.CTkEntry(self, width=250, height=30, placeholder_text="Enter a number of students or schools")
        self.Input.grid(row=0, padx=5, pady=10, sticky="ew")

        # Create a CTk Button
        self.button = ctk.CTkButton(
            master=self, text="Get matching", command=click_handler,
            fg_color="transparent", border_width=2, border_color='#15869d'
        )
        self.button.grid(row=1, padx=5, pady=10, sticky="ew")

        # Create a label for displaying the result
        self.output_label = ctk.CTkLabel(self, text='', justify='left', height=10)  # Set height to allow for multiple lines
        self.output_label.grid(row=2, padx=5, pady=10, sticky="ew")

        # Placeholder for students and schools (you need to define these variables)
        self.students = np.array([])
        self.schools = np.array([])

if __name__ == "__main__":
    app = App()
    app.mainloop()