class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = ['git', 'Пайтон для разработчиков']
        self.grades = {}
        self.courses_in_attack = ['Программировние на пайтон']

    def __str__(self):
        return (f"Student\nИмя: {self.name}\nФамилия: {self.surname}\nОбщая оценка: \nПройденные курсы"
                f"{self.courses_in_attack}\nКурсы в процессе изучения{self.courses_in_progress}")

    def rate_student(self, lecturer, course, grade):
        if isinstance(lecturer,
                      lecturer) and course in self.courses_in_attack and course in lecturer.courses_in_progress:
            if course in lecturer.gradess:
                lecturer.gradess[course] += [grade]
            else:
                lecturer.gradess[course] = [grade]
        else:
            return 'Ошибка'


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
        self.lectors_grade = {10, 9, 6}
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        nam = self.name
        sur = self.surname
        return (f"Lecturer\nИмя: {nam}\nФамилия: {sur}\nОбщая оценка: ")

arkadieprepod = Lecturer("Аркадий", "Поровозов")

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
    def __str__(self):
        return (f"Reviewer \nИмя: {self.name} \nФамилия: {self.surname}")


some_reviewer = Reviewer("Паша", "Техник")



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


print(some_reviewer)
print(onestuden)
print(arkadieprepod)