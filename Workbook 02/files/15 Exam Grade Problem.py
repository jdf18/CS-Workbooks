# Exam Grade Problem

# Write a function that returns the grade and the number of marks to the 
#  next grade from an exam result using the data below. The main program 
#  should output a suitable message to the student. E.g. A mark of 59 is 
#  grade 7. You needed 8 more marks for the next grade.

#   <2 |  2  |  4  |  13 |  22 |  31 |  41 |  54 |  67 |  80
# ----------------------------------------------------------
#   U  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  

grade_boundaries = {
    0:"U",2:"1",4:"2",13:"3",22:"4",
    31:"5",41:"6",54:"7",67:"8",80:"9",
}

def get_message(mark:int) -> str:
    for i, req_mark in enumerate(grade_boundaries.keys()):
        if req_mark > mark: break
    grade = tuple(grade_boundaries.values())[i-1]

    needed_marks = req_mark - mark

    print(f"A mark of {mark} is a grade {grade}. You needed \
{needed_marks} more marks for the next grade.")

get_message(59)