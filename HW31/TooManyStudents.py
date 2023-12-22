class TooManyStudents(Exception):

    def __str__(self):
        return "У группі не може бути більше 10 студентів!"