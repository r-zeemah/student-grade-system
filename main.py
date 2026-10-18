def get_average(scores):
    total_score = sum(scores)
    average = total_score / 3
    return round(average, 1)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def student_info (name, age, scores, total_score, average, grade, status):
    print("===== STUDENT GRADE REPORT =====")
    print("Name:", name)
    print("Age:", age)
    print("Scores:", scores)
    print("Total:", total_score)
    print("Average:", average)
    print("Grade:", grade)
    print("Status:", status)


students = []
again = "y"

while again == "y":
    name = input("Enter name:")

    while True:
        try:
            age = int(input("Enter age:"))
            break
        except ValueError:
            print("Please enter numbers only")

    scores = []
    for i in range(3):
        while True:
            try:
                score = int(input("Enter score:"))
                if score >= 0 and score <= 100:
                    break
                print("Score must be between 0 and 100")
            except ValueError:
                print("Please enter numbers only")
        scores.append(score)

    total_score = sum(scores)
    average = get_average(scores)
    grade = get_grade(average)

    if grade == "F":
        status = "Fail"
    else:
        status = "Pass"

    student_info(name, age, scores, total_score, average, grade, status)

    student = {"name": name, "age": age, "scores": scores, "average": average, "grade": grade}
    students.append(student)

    again = input("Add another student? (y/n): ").lower()