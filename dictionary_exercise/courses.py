courses = {}
command = input()
while command != 'end':
    splitted_command = command.split(' : ')
    course_name, student_name = splitted_command
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)
    command = input()
for course_name, student_name in courses.items():
    print(f"{course_name}: {len(student_name)}")
    for student in student_name:
        print(f"-- {student}")