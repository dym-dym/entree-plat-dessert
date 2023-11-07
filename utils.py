import numpy as np





def random_preferences(student_number, school_number):
    students = np.array([np.random.permutation(school_number) for x in range(student_number)])
    schools = np.array([np.random.permutation(student_number) for x in range(school_number)])

    return students, schools


def prefers(sender_1, sender_2, receiver):
    for x in receiver:
        if x == sender_1:
            return True
        elif x == sender_2: 
            return False
    raise ValueError("Unable to find preference order")



def get_matched_student(school, matches):
    for match in matches:
        if match[1] == school:
            return match[0]
    return -1


def get_matched_school(student, matches):
    for match in matches:
        if match[0] == student:
            return match[1]
    return -1


