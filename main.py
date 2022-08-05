class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_in_attack = ['Программировние на пайтон']

    def gr_student(self):
        sum_grade = 0
        grafes = 0
        for course in self.grades.values():
            sum_grade += sum(course)
            grafes += len(course)
        return sum_grade / grafes



    def __str__(self):
        return (f"Student\nИмя: {self.name}\nФамилия: {self.surname}\nОбщая оценка:{self.gr_student()} \nПройденные курсы"
                f"{self.courses_in_attack}\nКурсы в процессе изучения{self.courses_in_progress}")

    def rate_student(self, lecturer, course, lectors_grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress:
            if course in lecturer.lectors_grade:
                lecturer.lectors_grade[course] += [lectors_grade]
            else:
                lecturer.lectors_grade[course] = [lectors_grade]
        else:
            return 'Ошибка'

    def __lt__(self, dark_student):
        sravni = self.gr_student() < dark_student.gr_student()
        return sravni

onestuden = Student("Игорь", "Куращуп", "")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        nam = self.name
        sur = self.surname
        return f"Имя: {nam},Фамилия: {sur} "


class Lecturer(Mentor):
    def __init__(self, name, surname, ):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.lectors_grade = {}
    def rate_hwe(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course :
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



    def sum_grades(self):
        sum_grade = 0
        col = 0
        for course in self.lectors_grade.values():
            sum_grade += sum(course)
            col += len(course)
        return sum_grade / col



    def __lt__(self, two_lektor):
        sravnenie = self.sum_grades() < two_lektor.sum_grades()

        return sravnenie

    def __str__(self):
        nan = (f"Lecturer\nИмя: {self.name}\nФамилия: {self.surname}\nОбщая оценка: {self.sum_grades()}")
        return nan

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f"Reviewer \nИмя: {self.name} \nФамилия: {self.surname}")


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['git']

dark_student = Student('Dart', 'Veider', 'your_gender')
dark_student.courses_in_progress += ['Python']
dark_student.courses_in_progress += ['git']

cool_Lecturer = Lecturer('Some', 'Buddy')
cool_Lecturer.courses_attached += ['Python']
cool_Lecturer.courses_attached += ['git']

best_student.rate_student(cool_Lecturer, 'git', 10)
best_student.rate_student(cool_Lecturer, 'git', 6)
best_student.rate_student(cool_Lecturer, 'git', 8)

cool_Lecturer.rate_hwe(best_student, 'Python', 10)
cool_Lecturer.rate_hwe(best_student, 'Python', 9)
cool_Lecturer.rate_hwe(best_student, 'Python', 10)

cool_Lecturer.rate_hwe(best_student, 'git', 5)
cool_Lecturer.rate_hwe(best_student, 'git', 9)
cool_Lecturer.rate_hwe(best_student, 'git', 10)

cool_Lecturer.rate_hwe(dark_student, 'Python', 10)
cool_Lecturer.rate_hwe(dark_student, 'Python', 9)
cool_Lecturer.rate_hwe(dark_student, 'Python', 10)

cool_Lecturer.rate_hwe(dark_student, 'git', 10)
cool_Lecturer.rate_hwe(dark_student, 'git', 10)
cool_Lecturer.rate_hwe(dark_student, 'git', 10)

two_lektor = Lecturer('Somes', 'Buddyb')
two_lektor.courses_attached += ['Python']
two_lektor.courses_attached += ['git']

best_student.rate_student(two_lektor, 'git', 10)
best_student.rate_student(two_lektor, 'git', 5)
best_student.rate_student(two_lektor, 'git', 8)

hew_revier = Reviewer('Джек', 'Воробей')

print(f"{best_student}\nЛучший студент в аккадемии:{best_student > dark_student}\n")

print(f'{cool_Lecturer}\nЛучший лектор в аккадемии:{cool_Lecturer > two_lektor}\n' )

print(hew_revier)
