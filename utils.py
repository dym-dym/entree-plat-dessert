import numpy as np





def random_preferences(student_number : int , school_number : int) -> tuple[np.ndarray, np.ndarray]:
    """
    Generates a random set of preferences for given numbers of students/schools

    :param student_number: (int) Number of students
    :param school_number: (int) Number of schools
    :return: students : a Numpy array of student_number arrays, each being a random permutation of school IDs
             schools : a Numpy array of school_number arrays, each being a random permutation of student IDs
    """ 

    students = np.array([np.random.permutation(school_number) for x in range(student_number)])
    schools = np.array([np.random.permutation(student_number) for x in range(school_number)])

    return students, schools



def prefers(student_1 : int, student_2 : int, school : list[int]) -> bool:
    """
    Tells which of two students is preferred by a given receiver

    :param student_1: (int) First student ID
    :param student_2: (int) Second student ID
    :return: (bool) True if school prefers student_1 to student_2, False otherwise
    """ 
    
    for x in school:
        if x == student_1:
            return True
        elif x == student_2: 
            return False
    raise ValueError("Unable to find preference order")



def get_matched_student(school : int, matches : list[tuple[int,int]]) -> int:
    """
    Given a list of matches and a school, returns the student matched with that school (if he exists)

    :param school: (int) School ID
    :param matches: (list[tuple[int,int]]) A list of matches
    :return: (int) The ID (int) of the student matched with school if he exists, -1 otherwise
    """ 

    for match in matches:
        if match[1] == school:
            return match[0]
    return -1


def get_matched_school(student : int, matches : list[tuple[int,int]]) -> int:
    """
    Given a list of matches and a student, returns the school matched with that student (if it exists)

    :param student: (int) Student ID
    :param matches: (list[tuple[int,int]]) A list of matches
    :return: (int) The ID (int) of the school matched with student if it exists, -1 otherwise
    """ 

    for match in matches:
        if match[0] == student:
            return match[1]
    return -1


