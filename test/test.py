from matching import *
from utils import *
import sys



def is_everyone_matched(matches, students, schools):
    all_matched = True
    for st_index in range(len(students)):
        if(get_matched_school(st_index, matches) < 0):
            print(f'Student {st_index} is unmatched')
            all_matched = False
    for sc_index in range(len(schools)):
        if(get_matched_student(sc_index, matches) < 0):
            print(f'School {sc_index} is unmatched')
            all_matched = False
    return all_matched



def is_matching_stable(matches, students, schools):
    stable = True
    for st_index in range(len(students)):
        matched_school = get_matched_school(st_index, matches)
        for preferred_school in students[st_index]:
            if preferred_school == matched_school:
                break
            matched_student = get_matched_student(preferred_school, matches)
            if prefers(st_index, matched_student, schools[preferred_school]):
                print(f'Unstability : student {st_index} prefers school {preferred_school} over {matched_school} and school {preferred_school} prefers student {st_index} over {matched_student}')
                stable = False
    return stable




def random_test(student_number, school_number):
    students, schools = random_preferences(student_number, school_number)
    print("Students :")
    print(students)
    print("Schools :")
    print(schools)

    matches = stable_marriage(students, schools)

    print("Matching found :")
    print(matches)

    if(not is_everyone_matched(matches, students, schools)):
        print("Not everyone is matched")
        return False

    if(not is_matching_stable(matches, students, schools)):
        print("Matching is unstable")
        return False


    print("Matching is complete and stable")
    return True



if(len(sys.argv) != 4):
    print(f'Use : python -m test.test student_number school_number batch_size')

student_number = int(sys.argv[1])
school_number = int(sys.argv[2])
test_batch_size = int(sys.argv[3])

successes = 0

for i in range(test_batch_size):
    print(f'===================\nTest {i}')
    if(random_test(student_number, school_number)):
        successes += 1
    
print(f'===================\n{successes}/{test_batch_size} passed')
