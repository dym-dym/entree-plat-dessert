import numpy as np

from utils import get_matched_student, prefers



def stable_marriage(students, schools):
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
                    raise UserWarning("Unmatched student n° {} left with no school choice !".format(st_index))
                    students_free[st_index] = False 
    return matches

