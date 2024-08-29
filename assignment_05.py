# ------------------------------------------------------------------------------------------ #
# Title: Assignment05.py
# Desc: This assignment demonstrates managing student course registrations with options to register, display, and save data to a CSV file.
# Change Log: (Who, When, What)
#  Priya, 8/28/2024, Updated Script with additional error handling and functionalities
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ""  
student_last_name: str = ""  
course_name: str = ""  
csv_data: str = "" 
file = None 
menu_choice: str = "" 
student_data: list = []  
students: list[list[str]] = []

# Load data from the CSV file when the program starts
try:
    with open(FILE_NAME, 'r') as file_obj:
        for row in file_obj:
            parts = row.strip().split(',')
            if len(parts) == 3:
                students.append(parts)
except FileNotFoundError:
    print(f"File {FILE_NAME} not found. Starting with an empty list.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Present and process the data
while True:
    # Present the menu choices
    print(MENU)
    menu_choice = input("What would you like to do: ").strip()

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter student's first name: ").strip()
            if not student_first_name:
                raise ValueError("First name cannot be empty.")
            student_last_name = input("Enter student's last name: ").strip()
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")
            course_name = input("Enter course name: ").strip()
            if not course_name:
                raise ValueError("Course name cannot be empty.")

            student_data = [student_first_name, student_last_name, course_name]
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Present the current data
    elif menu_choice == "2":
        print("\nThe current data is:")
        if students:
            for student in students:
                print(f"{student[0]}, {student[1]} is enrolled in {student[2]}")
        else:
            print("No data to display.")
        print()

    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, 'w') as file_obj:
                for student in students:
                    file_obj.write(f"{student[0]},{student[1]},{student[2]}\n")
            print(f"Data has been saved to {FILE_NAME}.")
        except IOError as io_err:
            print(f"File error: {io_err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Exit the program
    elif menu_choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Please only choose option 1, 2, 3, or 4.")

print("Program Ended")
