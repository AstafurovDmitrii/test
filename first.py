class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_courses if total_courses != 0 else 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.finished_courses = []
        self.courses_in_progress = []

    def average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_courses if total_courses != 0 else 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\n'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_hw_grade(students, course):
    total_grades = sum(sum(student.grades.get(course, [])) for student in students)
    total_students = sum(1 for student in students if course in student.grades)
    return total_grades / total_students if total_students != 0 else 0


def average_lecture_grade(lecturers, course):
    total_grades = sum(sum(lecturer.grades.get(course, [])) for lecturer in lecturers)
    total_lecturers = sum(1 for lecturer in lecturers if course in lecturer.grades)
    return total_grades / total_lecturers if total_lecturers != 0 else 0


# Создаем экземпляры классов
student1 = Student('Ruoy', 'Eman', 'М')
student2 = Student('Dima', 'Ergan', 'М')
lecturer1 = Lecturer('Dima', 'Snow')
lecturer2 = Lecturer('Dima', 'Olegovith')
reviewer1 = Reviewer('Oleg', 'Snow')
reviewer2 = Reviewer('Denis', 'Wolk')

# Присваиваем оценки и курсы
student1.grades = {'Python': [7, 1, 5, 7, 2, 8]}
student1.finished_courses.append("git")
student1.courses_in_progress = ['Java']
student2.grades = {'git': [8, 7, 5, 4, 6, 5]}
student2.finished_courses.append("python с нуля")
student2.courses_in_progress = ['git']
lecturer1.grades = {'Java': [5, 10, 11, 7]}
lecturer1.finished_courses.append('C++')
lecturer1.courses_in_progress = ['Paskal']
lecturer2.grades = {'Paskal': [8, 3, 12, 13]}
lecturer2.finished_courses.append('HTML')
lecturer2.courses_in_progress = ['HTML']
reviewer1.courses_attached = ['Paskal']
reviewer2.courses_attached = ['HTML']

# Вызываем методы
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)
print(student1.rate_lecturer(lecturer1, "Java", 8))
print(student2.rate_lecturer(lecturer2, "HTML", 9))
print(average_hw_grade([student1, student2], "Python"))
print(average_lecture_grade([lecturer1, lecturer2], "Paskal"))
