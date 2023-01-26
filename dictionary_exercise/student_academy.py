students = {}
count_of_pairs = int(input())


def get_average_grade(grades, count_of_grades):
    average_grade = grades / count_of_grades
    return float(average_grade)


for i in range(count_of_pairs):
    current_student = input()
    current_grade = float(input())
    if current_student not in students.keys():
        students[current_student] = [current_grade]
    else:
        students[current_student].append(current_grade)
for student in students.keys():
    if get_average_grade(sum(students[student]), len(students[student])) >= 4.50:
        print(f"{student} -> {(get_average_grade(sum(students[student]), len(students[student]))):.2f}")
