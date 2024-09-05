# ---------------------------------------------------------------------------- #
# Title: Assignment06
# Description: A program to manage student course registrations.
# ChangeLog (Who, When, What):
# Priya Tomar, 09/04/2024, Created script to meet the assignment requirements
# ---------------------------------------------------------------------------- #

import json

# Constants
MENU: str = '''---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------'''
FILE_NAME: str = "Enrollments.json"

# Variables
menu_choice: str = ""
students: list = []

class FileProcessor:
   

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        
        try:
            with open(file_name, "r") as file:
                student_data.extend(json.load(file))
        except FileNotFoundError as e:
            IO.output_error_messages(f"Error: {file_name} not found.", e)
        except json.JSONDecodeError as e:
            IO.output_error_messages(f"Error: Could not decode JSON in {file_name}.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            print(f"Data saved to {file_name}.")
        except Exception as e:
            IO.output_error_messages(f"Error: Could not write to {file_name}.", e)

class IO:
    

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
       
        print(f"{message}\nException: {error}")

    @staticmethod
    def output_menu(menu: str):
        
        print(menu)

    @staticmethod
    def input_menu_choice():
        
        return input("Enter your choice [1-4]: ").strip()

    @staticmethod
    def output_student_courses(student_data: list):
        
        if not student_data:
            print("No student data available.")
        else:
            for student in student_data:
                print(f"{student['FirstName']} {student['LastName']} is registered for {student['CourseName']}")

    @staticmethod
    def input_student_data(student_data: list):
        
        try:
            first_name = input("Enter the student's first name: ").strip()
            last_name = input("Enter the student's last name: ").strip()
            course_name = input("Enter the course name: ").strip()
            student_data.append({"FirstName": first_name, "LastName": last_name, "CourseName": course_name})
        except Exception as e:
            IO.output_error_messages("Error: Invalid input.", e)

# Main Program
FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)
    elif menu_choice == "2":
        IO.output_student_courses(students)
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif menu_choice == "4":
        print("Program Ended!")
        break
    else:
        print("Invalid choice.")
