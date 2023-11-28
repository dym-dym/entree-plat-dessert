import tkinter as tk
import customtkinter as ctk
from utils import *
from matching import *
import os
from test_output import *
from plot_curves import satisfaction_curve

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Projet HAI902I: Aide à la décision')
        self.geometry("720x720")
        self.grid_columnconfigure((0, 3), weight=1)

        def get_matching():
            input_value = self.Input.get()

            try:
                input_value = int(input_value)
                result_file = "matching_results.txt"
                random_test(input_value, input_value, result_file)

                with open(result_file, "r") as file:
                    lines = file.readlines()
                    filtered_lines = [line.strip() for line in lines if not line.startswith("Student average satisfaction:")
                                                                        and not line.startswith("School average satisfaction:")
                                                                        and line.strip()]

                    result_text = "\n".join(filtered_lines)
                self.output_label_matching.configure(text=result_text)

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        def get_satisfactions():
            input_value = self.Input.get()

            try:
                input_value = int(input_value)
                result_file = "matching_results.txt"
                random_test(input_value, input_value, result_file)

                with open(result_file, "r") as file:
                    lines = file.readlines()
                    student_lines = [line.strip() for line in lines if line.startswith("Student average satisfaction:")]
                    school_lines = [line.strip() for line in lines if line.startswith("School average satisfaction:")]

                    result_text = "\n".join(student_lines + school_lines)
                self.output_label_satisfaction.configure(text=result_text)

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        def show_graph():
            input_value = self.Input.get()

            try:
                result_file = "matching_results.txt"

                # Additional input for tests_per_size
                tests_per_size = int(self.TestsPerSize.get())
                
                # Input for size_start
                size_start = int(self.SizeStart.get())

                # Input for size_end
                size_end = int(self.SizeEnd.get())

                # Ensure the 'figs' directory exists
                os.makedirs('figs', exist_ok=True)

                # Generate the graph based on the input values
                satisfaction_curve(size_start, size_end, tests_per_size)

                # Wait for a moment to ensure the image is saved
                self.after(100, lambda: self.display_graph(size_start, size_end, tests_per_size))

            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        def display_graph(self, size_start, size_end, tests_per_size):
            # Create a standard tkinter Canvas
            graph_canvas = tk.Canvas(self)
            graph_canvas.grid(row=11, padx=5, pady=10, columnspan=2, sticky="ew")

            # Read the image and display it on the canvas
            img_path = f"figs/curve_{size_start}_{size_end}_{tests_per_size}.png"
            img = tk.PhotoImage(file=img_path)
            graph_canvas.create_image(10, 10, anchor=tk.NW, image=img)
            graph_canvas.img = img

        # Make a title on the page
        self.title_label = ctk.CTkLabel(
            self, text="Voici une implémentation de l'algorithme de mariage stable entre étudiants et établissements."
                        '\n' " Veuillez rentrer une valeur correspondant aux nombre d'étudiants et d'écoles que vous souhaitez mettre en relation :"
        )
        self.title_label.grid(row=0, padx=5, pady=10, columnspan=2)

        # Create an input
        self.Input = ctk.CTkEntry(
            self, width=250, height=30, placeholder_text="Number of students or schools"
        )
        self.Input.grid(row=1, padx=5, pady=10, sticky="ew", columnspan=2)

        # Create CTk Buttons
        self.button_stats = ctk.CTkButton(
            master=self, text="Get the satisfactions", command=get_satisfactions,
            fg_color="transparent", border_width=2, border_color='#15869d', width=150
        )
        self.button_stats.grid(row=2, padx=2, pady=2, columnspan=1)

        # Create a frame for displaying the statistics of the matching
        self.frame = ctk.CTkFrame(self, width=30)
        self.frame.grid(row=3, padx=5, pady=10, columnspan=2, sticky="ew")

        # Create a label for displaying the satisfactions in a simple frame
        self.output_label_satisfaction = ctk.CTkLabel(self.frame, text='', justify='left')
        self.output_label_satisfaction.pack(fill='both', expand=True)

        # Create a scrollable frame for displaying the result
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=30)
        self.scroll_frame.grid(row=5, padx=2, pady=10, columnspan=2, sticky="ew")

        # Create a label for displaying the result within the scroll frame
        self.output_label_matching = ctk.CTkLabel(self.scroll_frame, text='', justify='left')
        self.output_label_matching.pack(fill='both', expand=True)

        # Create CTk Button for getting matching results
        self.button_matching = ctk.CTkButton(
            master=self, text="Get matching", command=get_matching,
            fg_color="transparent", border_width=2, border_color='#15869d', width=100
        )
        self.button_matching.grid(row=4, padx=4, pady=2, columnspan=2)

        self.test_label = ctk.CTkLabel(
            self, text="Affichage de la moyenne de N tests de satisfactions sur des jeux de données de taille différente. \n "
            "Il faut entrer la taille minimale et maximale des jeux de données, ainsi que le nombre de tests souhaités. "
        )
        self.test_label.grid(row=6, padx=5, pady=10, columnspan=2)

        # Create an input for size_start
        self.SizeStart = ctk.CTkEntry(
            self, width=250, height=30, placeholder_text="Minimal size of the test batch"
        )
        self.SizeStart.grid(row=7, padx=5, pady=10, sticky="ew", columnspan=2)

        # Create an input for size_end
        self.SizeEnd = ctk.CTkEntry(
            self, width=250, height=30, placeholder_text="Maximal size of the tests batch"
        )
        self.SizeEnd.grid(row=8, padx=5, pady=10, sticky="ew", columnspan=2)

        # Create an input for tests_per_size
        self.TestsPerSize = ctk.CTkEntry(
            self, width=250, height=30, placeholder_text="Number of tests for the graph"
        )
        self.TestsPerSize.grid(row=9, padx=5, pady=10, sticky="ew", columnspan=2)

        # Create a button for showing the graph
        self.button_show_graph = ctk.CTkButton(
            master=self, text="Show Graph", command=show_graph,
            fg_color="transparent", border_width=2, border_color='#15869d', width=100
        )
        self.button_show_graph.grid(row=10, padx=2, pady=2, columnspan=2)

        # Placeholder for students and schools (you need to define these variables)
        self.students = np.array([])
        self.schools = np.array([])

if __name__ == "__main__":
    app = App()
    app.mainloop()
