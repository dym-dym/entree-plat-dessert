from matching import *
from utils import *

import sys
import matplotlib.pyplot as plt




def satisfaction_curve(size_start : int, size_end : int, tests_per_size : int):
    student_satisfaction_array = []
    school_satisfaction_array = []

    print(f"Size : 0, test 0/{tests_per_size}", end="\r")

    for size in range(size_start, size_end):
        student_satisfaction_sum = 0
        school_satisfaction_sum = 0
        for test_i in range(tests_per_size):
            students, schools = random_preferences(size, size)
            matches = stable_marriage(students, schools)
            student_scores, school_scores = satisfaction(matches, students, schools)
            student_satisfaction_sum += np.mean(student_scores)
            school_satisfaction_sum += np.mean(school_scores)
            print(f"Size : {size}, test {test_i+1}/{tests_per_size}", end="\r")
        student_satisfaction_array.append(student_satisfaction_sum / tests_per_size)
        school_satisfaction_array.append(school_satisfaction_sum / tests_per_size)
        

    plt.figure()
    plt.plot(student_satisfaction_array, color='blue')
    plt.plot(school_satisfaction_array, color='red')
    plt.show()
    plt.savefig(f"figs/curve_{size_start}_{size_end}_{tests_per_size}.png")





if __name__ == "__main__":
    if(len(sys.argv) != 4):
        print(f'Use : python -m test.plot_curves size_start size_end tests_per_size')

    size_start = int(sys.argv[1])
    size_end = int(sys.argv[2])
    tests_per_size = int(sys.argv[3])

    satisfaction_curve(size_start, size_end, tests_per_size)
