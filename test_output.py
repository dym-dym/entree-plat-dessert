from matching import *
from utils import *
import sys

def is_everyone_matched(matches: list[tuple[int, int]], students: np.ndarray, schools: np.ndarray) -> bool:
    """
    Tests if each student and each school has a match in matches

    :param matches : (list[tuple[int,int]]) A list of (student,school) tuples representing matches between the two sets
    :param students : a Numpy array of student_number arrays, each being a an ordered preference array of school IDs
    :param schools : a Numpy array of school_number arrays, each being an ordered preference array of student IDs
    :return: (bool) True if everyone has a match, False if there is at least one student/school without a match
    """

    all_matched = True
    for st_index in range(len(students)):
        if get_matched_school(st_index, matches) < 0:
            print(f'Student {st_index} is unmatched')
            all_matched = False
    for sc_index in range(len(schools)):
        if get_matched_student(sc_index, matches) < 0:
            print(f'School {sc_index} is unmatched')
            all_matched = False
    return all_matched


def is_matching_stable(matches: list[tuple[int, int]], students: np.ndarray, schools: np.ndarray) -> bool:
    """
    Tests if the given matching is stable with regard to the set of preferences.
    A matching is said unstable if there exists a student A and a school B such that :
    1) A prefers B over its current match
    and
    2) B also prefers A over its current match

    :param matches : (list[tuple[int,int]]) A list of (student,school) tuples representing matches between the two sets
    :param students : a Numpy array of student_number arrays, each being a an ordered preference array of school IDs
    :param schools : a Numpy array of school_number arrays, each being an ordered preference array of student IDs
    :return: (bool) True if the matching is stable, False if there is at least one unstable pairing
    """

    stable = True
    for st_index in range(len(students)):
        matched_school = get_matched_school(st_index, matches)
        for preferred_school in students[st_index]:
            if preferred_school == matched_school:
                break
            matched_student = get_matched_student(preferred_school, matches)
            if prefers(st_index, matched_student, schools[preferred_school]):
                print(
                    f'Unstability : student {st_index} prefers school {preferred_school} over {matched_school} and school {preferred_school} prefers student {st_index} over {matched_student}')
                stable = False
    return stable

def write_result(matches, student_avg, school_avg, result_file="matching_results.txt"):
    # Save results to a file
    with open(result_file, "w") as file:
        file.write(f"Student average satisfaction: {student_avg:.3f}\n")
        file.write(f"\nSchool average satisfaction: {school_avg:.3f}\n")
        file.write(f"\n\nMatching results:\n")
        for student, school in matches:
            file.write(f"Student {student} matches with School {school}\n")
    


def random_test(student_number, school_number, result_file="matching_results.txt"):
    """
    Runs the matching algorithm on a randomly generated set of preferences and test the validity of the matching

    :param student_number: (int) Number of students
    :param school_number: (int) Number of schools
    :param result_file: (str) File to save the matching results
    :return: (bool) True if the matching returned is valid (complete and stable), False otherwise
    """
    students, schools = random_preferences(student_number, school_number)
    print("Students :")
    print(students)
    print("Schools :")
    print(schools)

    matches = stable_marriage(students, schools)

    print("Matching found :")
    print(matches)

    if not is_everyone_matched(matches, students, schools):
        print("Warning : Not everyone is matched")
        complete = False
    else:
        complete = True

    if not is_matching_stable(matches, students, schools):
        print("Matching is unstable")
        return False

    student_scores, school_scores = satisfaction(matches, students, schools)
    print(student_scores, school_scores)
    student_avg = np.mean(student_scores)
    school_avg = np.mean(school_scores)
    print(f"Student average satisfaction : {student_avg:.3f}")
    print(f"School average satisfaction : {school_avg:.3f}")

    if complete:
        print("Matching is complete and stable")
    else:
        print("Matching is stable, but not complete")

    # Save results to a file
    write_result(matches, student_avg, school_avg, result_file=result_file)

    return True


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f'Use : python -m test.test student_number school_number batch_size')

    student_number = int(sys.argv[1])
    school_number = int(sys.argv[2])
    test_batch_size = int(sys.argv[3])

    successes = 0

    for i in range(test_batch_size):
        print(f'===================\nTest {i}')
        if random_test(student_number, school_number):
            successes += 1

    print(f'===================\n{successes}/{test_batch_size} passed')
