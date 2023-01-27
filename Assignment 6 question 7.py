class Student:
    pass

class Marks:
    pass

student_1 = Student()
marks_1 = Marks()

# check if student_1 is an instance of Student class
print(isinstance(student_1, Student)) # True

# check if marks_1 is an instance of Marks class
print(isinstance(marks_1, Marks)) # True

# check if Student is a subclass of object class
print(issubclass(Student, object)) # True

# check if Marks is a subclass of object class
print(issubclass(Marks, object)) # True
