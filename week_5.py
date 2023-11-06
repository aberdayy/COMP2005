'''
1.Define 2 classes: Student and Course
    class Course:
        code: string
        name: string
        room: string
        credits: integer

        class Student:
            student id: string
            student name: string
            courses enrolled: list of Course
2.Define all required methods
3.Define enroll method for students
    a list of courses and course code of the enrolled course is the parameter
    finds the course in the course lists, and adds the course to enrolled courses.


'''
class Course:
    def __init__(self, code = "", name =  "", room= "", course_credits = 0):
        self.code = code
        self.name = name
        self.room = room
        self.course_credits = course_credits

    # getter
    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

    def get_room(self):
        return self.room

    def get_course_credits(self):
        return self.course_credits

    # setter
    def set_code(self, code):
        self.code = code

    def set_name(self,name):
        self.name = name

    def set_room(self,room):
        self.room = room

    def set_course_credits(self,course_credits):
        self.course_credits = course_credits

    # display method
    def display(self):
        print(f"Code: {self.code}, Name: {self.name}, Room: {self.room}, Credits: {self.course_credits}")

class Student:
    def __init__(self, student_id="", student_name="", courses_enrolled=[]):
        self.student_id = student_id
        self.student_name = student_name
        self.courses_enrolled = courses_enrolled

# getter
    def get_id(self):
        return self.student_id

    def get_name(self):
        return self.student_name

    def get_courses(self):
        return self.courses_enrolled

# setter
    def set_id(self, id):
        self.student_id = id

    def set_name(self, name):
        self.student_name = name

    def set_courses(self, course):
        self.courses_enrolled = course

    # enroll method
    def enroll_to_classes(self, courses, course_code):
        for c in courses:
            if c.get_code() == course_code:
                self.courses_enrolled.append(c)
                break

    # display method
    def display_courses(self):
        for c in self.get_courses():
            c.display()

    def display(self):
        print("Student ID:", self.get_id())
        print("      Name:", self.get_name())
        print("   Courses:")
        self.display_courses()


c1 = Course("MIS205", "Data Structures and Database Applications", "F303", 3)
c2 = Course("COMP2005", "Object Oriented Programming", "F323", 3)
c3 = Course("MIS201", "Network Systems", "B301", 3)
c4 = Course("COMP4005", "Computer Ethics and Law", "FL2-11", 2)
course_list = [c1, c2, c3, c4]
student = Student("111111111", "Ataberk Erday")
student.enroll_to_classes(course_list, c2.get_code())
student.enroll_to_classes(course_list, c3.get_code())
student.enroll_to_classes(course_list, c1.get_code())
student.display()
