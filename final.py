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