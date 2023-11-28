from utils import random_preferences
import sys
from serializer import write_preferences

if __name__ == "__main__":
    student_number = int(sys.argv[1])
    school_number = int(sys.argv[2])

    write_preferences("random_values.txt", *random_preferences(student_number, school_number))

