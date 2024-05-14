class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.point = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Student) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = 0
        for grade in self.grades:
            total_grades += grade
            result = total_grades / len(self.grades)
            return result
        
    def medal_1(self):
        total_point = 0
        for point in self.point:
         total_point += point
         result = total_point / len(self.point)
         return result

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return f'Имя:{self.name}\n' f'Фамилия:{self.surname}\n' f'Средняя оценка за лекции:{self.average_grade()}\n' f'Курсы в процессе изучения:{self.courses_in_progress}\n' f'Завершенные курсы:{self.finished_courses}\n' f'Средняя оценка за ДЗ:{self.medal_1()}\n'
    
    


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname,):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.finished_courses = []
        self.courses_in_progress = []

    def average_grade(self):
        total_grades = 0
        for grade in self.grades:
            total_grades += grade
            result = total_grades / len(self.grades)
            return result

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return f'Имя:{self.name}\n'f'Фамилия:{self.surname}\n' f'Средняя оценка за лекции:{self.average_grade()}\n'


class Reviewer(Mentor):
    def __init__(self, name, surname,):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя:{self.name}\n' f'Фамилия:{self.surname}\n'


Student_1 = Student('Ruoy', 'Eman', 'gender')
Student_1.grades = {7, 1, 5, 7, 2, 8}
Student_1.finished_courses.append("git")
Student_1.courses_attached = ['Java']
Student_1.courses_in_progress += ['Python']
Student_1.point = {7, 4, 1, 3, 2, 9}

Student_2 = Student('Dima', 'Ergan', 'gender')
Student_2.grades = {8, 7, 5, 4, 6, 5}
Student_2.finished_courses.append("python с нуля")
Student_2.courses_in_progress += ['git']
Student_2.courses_attached = ['Java']
Student_2.point = {4, 9, 9, 3, 2, 3}

Lecturer_1 = Lecturer('Dima', 'Snow',)
Lecturer_1.courses_attached = ['Java']
Lecturer_1.grades = {5, 10, 11, 7}
Lecturer_1.finished_courses = ['C++']
Lecturer_1.courses_in_progress = ['Paskal']

Lecturer_2 = Lecturer('Dima', 'Olegovith')
Lecturer_2.grades = {8, 3, 12, 13}
Lecturer_2.finished_courses = ['Paskal']
Lecturer_2.courses_in_progress = ['HTML']
Lecturer_2.courses_attached = ['C++']

Reviewer_1 = Reviewer('Oleg', 'Snow',)
Reviewer_1.courses_attached = ['Paskal']

Reviewer_2 = Reviewer('Denis', 'Wolk')
Reviewer_2.courses_attached = ['HTML']

print(Student_1)
print(Lecturer_1)
print(Reviewer_1)

print(Student_1.__gt__(Student_2))
print(Student_1.average_grade())
print(Student_1.rate_lecturer(lecturer = Lecturer_1 , course = "Java", grade = 8))
