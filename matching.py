import numpy as np

from utils import get_matched_student, prefers



def stable_marriage(students : np.ndarray, schools : np.ndarray) -> list[tuple[int,int]]:
    """
    Given a set of preferences, return a stable matching of students and schools using the Gale-Shapley algorithm

    :param students : a Numpy array of student_number arrays, each being a an ordered preference array of school IDs
    :param schools : a Numpy array of school_number arrays, each being an ordered preference array of student IDs
    :return: (list[tuple[int,int]]) A list of (student,school) tuples representing matches between the two sets
    """ 

    students_free = [True for x in students]
    schools_free = [True for x in schools]
    students = list(map(list, students))
    matches = []
    while True in students_free:
        for st_index in range(len(students)):
            if students_free[st_index]:
                if len(students[st_index]) > 0:
                    proposed_school = students[st_index][0]
                    existing_match = get_matched_student(proposed_school, matches)
                    if(existing_match < 0):
                        matches.append((st_index, proposed_school))
                        students_free[st_index] = False
                    else:
                        if prefers(st_index, existing_match, schools[proposed_school]):
                            matches.remove((existing_match, proposed_school))
                            students_free[existing_match] = True
                            matches.append((st_index, proposed_school))
                            students_free[st_index] = False
                    del(students[st_index][0])
                else:
                    print(f"Unmatched student n° {st_index} left with no school choice !")
                    students_free[st_index] = False 
    return matches

