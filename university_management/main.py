import streamlit as st

# University Management System
# This is a simple university management system that allows you to manage students, teachers, courses, and departments.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

class Student(Person):
    def __init__(self, name, age, rollNumber):
        super().__init__(name, age)
        self.rollNumber = rollNumber
        self.courses = []

    def registerForCourse(self, course):
        self.courses.append(course)

class Instructor(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = []

    def assignCourse(self, course):
        self.courses.append(course)

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructor = None

    def addStudent(self, student):
        self.students.append(student)

    def setInstructor(self, instructor):
        self.instructor = instructor

class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)


# Streamlit App
def main():
    st.set_page_config(page_title="University Management System", layout="wide")

    # Add a sidebar title and description with some color
    st.sidebar.markdown("<h1 style='text-align: center; color: #0d6efd;'>University Management System</h1>", unsafe_allow_html=True)
    menu = ["Home", "Students", "Teachers", "Courses", "Departments"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Home page
    if choice == "Home":
        st.markdown("<h2 style='text-align: center;'>Welcome to the University Management System</h2>", unsafe_allow_html=True)
        st.image("https://www.example.com/university_logo.jpg", use_column_width=True)

    # Students page
    elif choice == "Students":
        st.subheader("Manage Students")
        name = st.text_input("Enter student name")
        age = st.number_input("Enter student age", min_value=18)
        roll_number = st.text_input("Enter roll number")
        student = Student(name, age, roll_number)

        if st.button("Register Student", key="student_register"):
            st.success(f"Student {student.getName()} has been registered")
            st.write(f"Roll Number: {student.rollNumber}")

    # Teachers page
    elif choice == "Teachers":
        st.subheader("Manage Teachers")
        name = st.text_input("Enter Teacher name")
        age = st.number_input("Enter Teacher age", min_value=18)
        salary = st.number_input("Enter salary")
        teacher = Instructor(name, age, salary)

        if st.button("Register Teacher", key="teacher_register"):
            st.success(f"Teacher {teacher.getName()} has been registered")
            st.write(f"Salary: {teacher.salary}")

    # Courses page
    elif choice == "Courses":
        st.subheader("Manage Courses")
        course_name = st.text_input("Enter course name")
        course = Course(course_name)

        if st.button("Add Course", key="add_course"):
            st.success(f"Course {course.name} has been added")

    # Departments page
    elif choice == "Departments":
        st.subheader("Manage Departments")
        department_name = st.text_input("Enter department name")
        department = Department(department_name)

        if st.button("Add Department", key="add_department"):
            st.success(f"Department {department.name} has been added")


if __name__ == "__main__":
    main()

