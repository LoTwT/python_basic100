# 不同文件的关联

course_teacher_map = {}
with open("./p019/p019_course_teacher.txt", "r", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split(",")
        course_teacher_map[course] = teacher

with open("./p018/p018_course_student_grade_input.txt", "r", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        course, sno, sname, grade = line.split(",")
        teacher = course_teacher_map.get(course)
        print(course, teacher, sno, sname, grade)
