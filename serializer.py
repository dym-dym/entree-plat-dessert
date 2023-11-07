import numpy as np


def read_preferences(preference_file):
    with open(preference_file, 'r') as f:
        student_number = -1
        school_number = -1
        student_prefs = []
        school_prefs = []

        while student_number < 0:
            line = f.readline().rstrip().split()
            if(len(line) == 1):
                student_number = int(line[0])
        for i in range(student_number):
            student_prefs.append(list(map(int, f.readline().rstrip().split())))

        while school_number < 0:
            line = f.readline().rstrip().split()
            if(len(line) == 1):
                school_number = int(line[0])
        for i in range(school_number):
            school_prefs.append(list(map(int, f.readline().rstrip().split())))
        
        return np.array(student_prefs), np.array(school_prefs)





def write_preferences(preference_file, student_prefs, school_prefs):
    with open(preference_file, 'w') as f:
        f.write(f'{len(student_prefs)}\n')
        for student in student_prefs:
            f.write(" ".join(map(str, student)) + "\n")
        f.write(f'{len(school_prefs)}\n')
        for school in school_prefs:
            f.write(" ".join(map(str, school)) + "\n")
        