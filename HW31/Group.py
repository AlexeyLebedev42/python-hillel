import Student

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
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