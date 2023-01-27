def student_data(student_id, student_name = None, student_class = None):
    print("Student ID: ", student_id)
    if student_name != None:
        print("Student Name: ", student_name)
    if student_class != None:
        print("Student Class: ", student_class)

student_data(1) # Student ID: 1
student_data(1, student_name = "John") # Student ID: 1 Student Name: John
student_data(1, student_name = "John", student_class = "10th") # Student ID: 1 Student Name: John Student Class: 10th
