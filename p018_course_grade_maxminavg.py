# 计算班级的高分低分平均分
# key: course, value: grade list
course_grades = {}

with open("./p018_course_student_grade_input.txt", "r", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        course, sclass, sname, grade = line.split(",")
        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(int(grade))

for course, grades in course_grades.items():
    print(
        course,
        max(grades),
        min(grades),
        sum(grades) / len(grades)
    )
