import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from utils import *
from test_output import *
from plot_curves import *
from matching import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Projet HAI902I: Aide à la décision')
        self.geometry("1280x720")
        self.grid_columnconfigure((0, 1), weight=1)

        def get_matching():
            input_value = self.Input.get()

            try:
                input_value = int(input_value)  # Convert input to integer (assuming it's a number)
                result_file = "matching_results.txt"
                random_test(input_value, input_value, result_file)  # Use the input as both student_number and school_number

                # Read the results from the file
                with open(result_file, "r") as file:
                    lines = file.readlines()

                    # Exclude lines starting with the specified prefixes
                    filtered_lines = [line.strip() for line in lines if not line.startswith("Student average satisfaction:")
                                                                        and not line.startswith("School average satisfaction:")
                                                                        and line.strip()]

                    # Concatenate the filtered lines
                    result_text = "\n".join(filtered_lines)

                # Update the output label
                self.output_label_matching.configure(text=result_text)

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        def get_satisfactions():
            input_value = self.Input.get()

            try:
                input_value = int(input_value)  # Convert input to integer (assuming it's a number)
                result_file = "matching_results.txt"
                random_test(input_value, input_value, result_file)  # Use the input as both student_number and school_number

                # Read the results from the file
                with open(result_file, "r") as file:
                    lines = file.readlines()

                    # Filter lines starting with the specified prefixes
                    student_lines = [line.strip() for line in lines if line.startswith("Student average satisfaction:")]
                    school_lines = [line.strip() for line in lines if line.startswith("School average satisfaction:")]

                    # Concatenate the filtered lines
                    result_text = "\n".join(student_lines + school_lines)

                # Update the output label
                self.output_label_satisfaction.configure(text=result_text)

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        def show_graph(self):
            # Call the satisfaction_curve function with the Canvas as an argument
            satisfaction_curve(self.graph_canvas)


        # Make a title in the page
        self.title = ctk.CTkLabel(self, text="Voici une implémentation de l'algorithme de mariage stable entre étudiants et établissements."+'\n'+" Veuillez rentrer une valeur correspondant aux nombre d'étudiants et d'écoles que vous souhaitez mettre en relation :")
        self.title.grid(row=0, padx=5, pady=10)

        # Create an input
        self.Input = ctk.CTkEntry(self, width=250, height=30, placeholder_text="Enter a number of students or schools")
        self.Input.grid(row=1, padx=5, pady=10, sticky="ew")

        # Create CTk Buttons
        self.button_stats = ctk.CTkButton(
            master=self, text="Get the satisfactions", command=get_satisfactions,
            fg_color="transparent", border_width=2, border_color='#15869d', width=10
        )
        self.button_stats.grid(row=2, padx=2, pady=2, sticky="ew")

        self.button_matching = ctk.CTkButton(
            master=self, text="Get matching", command=get_matching,
            fg_color="transparent", border_width=2, border_color='#15869d', width=100
        )
        self.button_matching.grid(row=4, padx=4, pady=2, sticky="ew")



        # Create a scrollable frame for displaying the result
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=30)
        self.scroll_frame.grid(row=5, padx=2, pady=10, sticky="ew")

        # Create a frame for displaying the statistics of the matching
        self.frame = ctk.CTkFrame(self, width=30)
        self.frame.grid(row=3, padx=5, pady=10, sticky="ew")

        # Create a label for displaying the satisfactions in a simple frame 
        self.output_label_satisfaction = ctk.CTkLabel(self.frame, text='', justify='left')
        self.output_label_satisfaction.pack(fill='both', expand=True)
        
        # Create a label for displaying the result within the scroll frame
        self.output_label_matching = ctk.CTkLabel(self.scroll_frame, text='', justify='left')
        self.output_label_matching.pack(fill='both', expand=True)

    

        # Placeholder for students and schools (you need to define these variables)
        self.students = np.array([])
        self.schools = np.array([])

if __name__ == "__main__":
    app = App()
    app.mainloop()