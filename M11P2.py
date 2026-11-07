def compute_points(exam1, exam2, exam3):
    """Calculate total points and average together."""
    totalPoints = exam1 + exam2 + exam3
    average = totalPoints / 3
    return totalPoints, average

# Main Program
lastName = input("What is your last name? ")

totalPointExam1 = int(input("How many points did you get on the first exam? "))
totalPointExam2 = int(input("How many points did you get on the second exam? "))
totalPointExam3 = int(input("How many points did you get on the third exam? "))

totalPoints, average = compute_points(
    totalPointExam1,
    totalPointExam2,
    totalPointExam3
)
print()
print(f"Student with last name {lastName} has an average exam score of {average:.0f} with a total of {totalPoints} total points.")