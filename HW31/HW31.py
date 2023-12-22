class TooManyStudents(Exception):

    def __str__(self):
        return "У группі не може бути більше 10 студентів!"
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f" {self.gender}, {self.age}, {self.first_name}, {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__str__() == other.__str__()

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f"Student:{super().__str__()}, {self.record_book}\n"


class Group:
    max_students = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise TooManyStudents
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        if self.find_student(last_name):
            self.group.remove(self.find_student(last_name))

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f'{student.__str__()}\n'
        return f'Number:{self.number}\n{all_students}\n'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # Only one student