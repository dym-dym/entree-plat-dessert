import tkinter as tk
import customtkinter as ctk
from utils import *
from matching import *
import os
from test_output import *
from plot_curves import satisfaction_curve, satisfaction_histogram
from serializer import *
from pathlib import Path

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Projet HAI902I: Aide à la décision')
        self.geometry("720x720")
        self.grid_columnconfigure((0, 3), weight=1)

        self.random_pref = True


        def openFile():
            tf = ctk.filedialog.askopenfilename(
                initialdir="./", 
                title="Open Preference file", 
                filetypes=(("Text Files", "*.txt"),)
                )
            self.students, self.schools = read_preferences(tf)
            self.random_pref = False
            self.labelFileVar.set(Path(tf).name)
            self.Input.delete(0 ,'end')
        
        def save_prefs():
            tf = ctk.filedialog.asksaveasfilename(
                initialdir="./", 
                title="Save Preference file", 
                filetypes=(("Text Files", "*.txt"),)
                )
            write_preferences(tf, self.students, self.schools)

        def compute_matching():
            try:
                if self.random_pref:
                    input_value = self.Input.get()
                    input_value = int(input_value)
                    self.students, self.schools = random_preferences(input_value, input_value)
                else: 
                    self.random_pref = True
                
                result_file = "matching_results.txt"

                self.matches = stable_marriage(self.students, self.schools)
                
                if not is_everyone_matched(self.matches, self.students, self.schools):
                    print("Warning : Not everyone is matched")
                    complete = False
                else:
                    complete = True

                if not is_matching_stable(self.matches, self.students, self.schools):
                    print("Matching is unstable")
                    return False

                student_scores, school_scores = satisfaction(self.matches, self.students, self.schools)
                print(student_scores, school_scores)
                student_avg = np.mean(student_scores)
                school_avg = np.mean(school_scores)
                print(f"Student average satisfaction : {student_avg:.3f}")
                print(f"School average satisfaction : {school_avg:.3f}")

                write_result(self.matches, student_avg, school_avg, result_file=result_file)

            except ValueError:
                print("Invalid input. Please enter a valid number.")


        def get_matching():
            try:
                input_value = self.Input.get()
                compute_matching()

                result_file = "matching_results.txt"
                with open(result_file, "r") as file:
                    lines = file.readlines()
                    filtered_lines = [line.strip() for line in lines if not line.startswith("Student average satisfaction:")
                                                                        and not line.startswith("School average satisfaction:")
                                                                        and line.strip()]

                    matching_text = "\n".join(filtered_lines)

                    student_lines = [line.strip() for line in lines if line.startswith("Student average satisfaction:")]
                    school_lines = [line.strip() for line in lines if line.startswith("School average satisfaction:")]

                    satisfaction_text = "\n".join(student_lines + school_lines)

                self.output_label_matching.configure(text=matching_text)
                self.output_label_satisfaction.configure(text=satisfaction_text)

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        def show_graph():
            try:
                # Wait for a moment to ensure the image is saved
                self.after(100, lambda: display_graph())

            except ValueError:
                print("Invalid input. Please compute matching first")

        def display_graph():
            satisfaction_histogram(self.matches, self.students, self.schools)

        # Make a title on the page
        self.title_label = ctk.CTkLabel(
            self, text="Voici une implémentation de l'algorithme de mariage stable entre étudiants et établissements."
                        '\n' " Veuillez charger un fichier de préférences :"
        )
        self.title_label.grid(row=0, padx=5, pady=10, columnspan=2)

        # Create CTk Buttons
        self.button_loadfile = ctk.CTkButton(
            master=self, text="Load preferences", command=openFile,
            fg_color="transparent", border_width=2, border_color='#15869d', width=100
        )
        self.button_loadfile.grid(column=0, row=1, padx=2, pady=2, columnspan=2)

        self.labelFileVar = ctk.StringVar()
        self.labelFile = ctk.CTkLabel(self, textvariable=self.labelFileVar)
        self.labelFile.grid(column=0, row=1, padx=2, pady=2, columnspan=2, sticky="e")



        self.input_label = ctk.CTkLabel(
            self, text="Ou spécifiez un nombre d'étudiants/établissements\npour générer des préférences aléatoires : "
        )
        self.input_label.grid(row=2, column=0, padx=5, pady=10, columnspan=1, sticky="e")

        # Create an input
        self.Input = ctk.CTkEntry(
            self, width=250, height=30, placeholder_text="Number of students or schools"
        )
        self.Input.grid(row=2, column=1, padx=5, pady=10, sticky="ew", columnspan=1)

        # Create CTk Buttons
        self.button_matching = ctk.CTkButton(
            master=self, text="Get matching", command=get_matching,
            fg_color="transparent", border_width=2, border_color='#15869d', width=100
        )
        self.button_matching.grid(row=3, padx=2, pady=2, columnspan=2)

        # Create a frame for displaying the statistics of the matching
        self.frame = ctk.CTkFrame(self, width=30)
        self.frame.grid(row=4, padx=5, pady=10, columnspan=2, sticky="ew")

        # Create a label for displaying the satisfactions in a simple frame
        self.output_label_satisfaction = ctk.CTkLabel(self.frame, text='', justify='left')
        self.output_label_satisfaction.pack(fill='both', expand=True)

        # Create a scrollable frame for displaying the result
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=30, height=400)
        self.scroll_frame.grid(row=5, padx=2, pady=10, columnspan=2, sticky="ew")

        # Create a label for displaying the result within the scroll frame
        self.output_label_matching = ctk.CTkLabel(self.scroll_frame, text='', justify='left')
        self.output_label_matching.pack(fill='both', expand=True)

        # Create a button for showing the graph
        self.button_show_graph = ctk.CTkButton(
            master=self, text="Show Histogram", command=show_graph,
            fg_color="transparent", border_width=2, border_color='#15869d', width=100
        )
        self.button_show_graph.grid(column=0, row=11, padx=2, pady=2, columnspan=2)

        self.button_show_graph = ctk.CTkButton(
            master=self, text="Save preferences", command=save_prefs,
            fg_color="transparent", border_width=2, border_color='#15869d', width=100
        )
        self.button_show_graph.grid(column=1, row=11, padx=2, pady=2, columnspan=2)

        
        # Placeholder for students and schools (you need to define these variables)
        self.students = np.array([])
        self.schools = np.array([])

if __name__ == "__main__":
    app = App()
    app.mainloop()
