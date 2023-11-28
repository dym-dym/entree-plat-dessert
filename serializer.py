import numpy as np


def read_preferences(preference_file : str) -> tuple[np.ndarray, np.ndarray]:
    """
    Reads a set of student/school preferences from a file

    :param preference_file: (str) File to read from
    :return: student_prefs : a Numpy array of student preferences, each being an array of school IDs
             school_prefs : a Numpy array of school arrays, each being an array of student IDs
    """ 


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





def write_preferences(preference_file : str, student_prefs : np.ndarray, school_prefs : np.ndarray) -> None:
    """
    Writes a set of student/school preferences to a file

    :param preference_file: (str) File to write to
    :param student_prefs: (np.ndarray) Numpy array of student preferences
    :param school_prefs: (np.ndarray) Numpy array of school preferences
    :return: None
    """ 

    with open(preference_file, 'w') as f:
        f.write(f'{len(student_prefs)}\n')
        for student in student_prefs:
            f.write(" ".join(map(str, student)) + "\n")
        f.write(f'{len(school_prefs)}\n')
        for school in school_prefs:
            f.write(" ".join(map(str, school)) + "\n")
        