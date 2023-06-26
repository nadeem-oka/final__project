#Name :nadeem okasha
#Delivery Date :22-6-2023

import uuid

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark
class Student:
    total_students = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course Name: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        average = total_marks / len(self.courses_list)
        return average

students_list = []
while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
existing_student = next((student for student in students_list if student.student_number == student_number), None)
        if existing_student:
            print("Student Number already exists. Please enter a unique Student Number.")
        else:
            new_student = Student(student_name, student_age, student_number)
            students_list.append(new_student)
            print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number: ")

existing_student = next((student for student in students_list if student.student_number == student_number), None)
if existing_student:
    students_list.remove(existing_student)
    print("Student Deleted Successfully")
else:
    print("Student Not Exist")

elif selection == 3:
student_number = input("Enter Student Number: ")