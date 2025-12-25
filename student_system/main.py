

from utils import *

# File name constant
STUDENT_FILE = 'students.txt'


# Function for Add Student Records
def add_student():
    """
    Add a new student record to the system.
    """

    print("\n---------- Add Student Record ----------\n")

    while True:
        try:
            # Get student ID from user
            std_id = input("Enter Student ID (format: S001): ").strip()

            # Validate student ID format
            validate_student_id(std_id)

            std_id = std_id.upper()

            # Check if student ID already exists
            if check_duplicate_id(std_id):
                raise DuplicateIDError(std_id)

            break

        except FileNotFoundError:
            print("No student records file found. Please add students first.")

        except AssertionError as e:
            print(f"Error: {e}")
            print("Please try again!\n")

        except DuplicateIDError as e:
            print(f"Error: {e}")


    while True:
        try:
            # Get student name from user
            std_name = input("Enter Student Name: ").strip()

            # Validate student name
            validate_student_name(std_name)
            break

        except AssertionError as e:
            print(f"Error: {e}")
            print("Please try again!\n")


    while True:
        try:
            # Get Science marks from user
            s_marks = (int)(input("Enter Science Marks (0-100): ").strip())
            
            # Validate marks
            validate_marks(s_marks)   
            break

        except ValueError:
            print("Error: Invalid mark. Marks should be integers between 0 and 100.")
            print("Please try again!\n")

        except InvalidMarkError as e:
            print(f"Error: {e}")
            print("Please try again!\n")


    while True:
        try:
            # Get Maths marks from user
            m_marks = (int)(input("Enter Maths Marks (0-100): ").strip())

            # Validate marks
            validate_marks(m_marks)
            break

        except ValueError:
            print("Error: Invalid mark. Marks should be integers between 0 and 100.")
            print("Please try again!\n")

        except InvalidMarkError as e:
            print(f"Error: {e}")
            print("Please try again!\n")


    student = {
        "Student_ID": std_id,
        "Student_Name": std_name,
        "Science": (s_marks),
        "Maths": (m_marks)
    }

    write_students_file(STUDENT_FILE, [student])    
    print("\nStudent record added successfully!")


# Function for View All Student Records
def view_all_students():
    """
    View all student records from the file
    """

    print("\n---------- View All Student Records ----------\n")

    students = read_students_file(STUDENT_FILE)

    # Check if there are any students
    if not students:
        print("No student records found.")
        return

    display_student_table_header()

    for student in students:
        display_student_row(student)

    display_student_table_footer()


# Function for Search Student by ID
def search_student():
    """
    Search for a student record using Student ID
    """
    print("\n---------- Search Student by ID ----------\n")

    while True:
        try:
            std_id = input("Enter Student ID to search: ").strip()
                
            # Validate student ID
            validate_student_id(std_id)

            std_id = std_id.upper()

            # Track student record status
            status = False
            s_found = None

            students = read_students_file(STUDENT_FILE)

            for student in students:
                if student['Student_ID'] == std_id:
                    status = True
                    s_found = student
                    break

            if status:
                print("Student record found!\n")
                print("---------- Student Record ----------\n")
                display_student_table_header()
                display_student_row(s_found)
                display_student_table_footer()
                break
            else:
                print("Student record not found.")
                break

        except FileNotFoundError:
            print("No student records file found. Please add students first.")

        except AssertionError as e:
            print(f"Error: {e}")
            print("Please try again!\n")

            # Ask user if they want to try again
            retry = input("Would you like to try again? (y/n): ").strip().lower()

            if retry == 'y':
                print()
                continue
            elif retry == 'n':
                print("Returning to main menu...")
                return
            else:
                print("Invalid input. Returning to main menu...")
                return


# Function for Update Student Marks
def update_student():
    """
    Update a student record using Student ID
    """
    print("\n---------- Update Student Marks ----------\n")

    while True:
        try:
            # Get student ID to update
            std_id = input("Enter Student ID to update: ").strip()
            
            # Validate student ID
            validate_student_id(std_id)
            
            std_id = std_id.upper()
            
            # Read all students
            students = read_students_file(STUDENT_FILE)
            
            # Check if file is empty
            if not students:
                print("No student records found.")
                return
            
            # Search for the student and get the index if found
            # used enumerate() to get index and value
            f_index = -1
            for i, student in enumerate(students): 
                if student['Student_ID'] == std_id:
                    f_index = i
                    break
            
            # Check if student was found
            if f_index == -1:
                print(f"Student record not found for ID: {std_id}")
                break
            
            # Display current record
            c_std = students[f_index]

            print("\n---------- Current Student Record ----------\n")
            display_student_table_header()
            display_student_row(c_std)
            display_student_table_footer()
            print()

            # Get new Science marks
            while True:
                try:
                    new_s_marks = int(input("Enter new Science Marks (0-100): ").strip())
                    validate_marks(new_s_marks)
                    break
                
                except ValueError:
                    print("Error: Invalid mark. Marks should be integers between 0 and 100.")
                    print("Please try again!\n")
                
                except InvalidMarkError as e:
                    print(f"Error: {e}")
                    print("Please try again!\n")
            
            # Get new Maths marks
            while True:
                try:
                    new_m_marks = int(input("Enter new Maths Marks (0-100): ").strip())
                    validate_marks(new_m_marks)
                    break
                
                except ValueError:
                    print("Error: Invalid mark. Marks should be integers between 0 and 100.")
                    print("Please try again!\n")
                
                except InvalidMarkError as e:
                    print(f"Error: {e}")
                    print("Please try again!\n")
            
            # Update the student record
            students[f_index]['Science'] = new_s_marks
            students[f_index]['Maths'] = new_m_marks
            
            # Write updated records back to file using your new function
            write_all_students_file(STUDENT_FILE, students)
            
            print("\nStudent marks updated successfully!")
            
            # Display updated record
            print("\n---------- Updated Student Record ----------\n")
            display_student_table_header()
            display_student_row(students[f_index])
            display_student_table_footer()
            break
        
        except FileNotFoundError:
            print("No student records file found. Please add students first.")
            break
        
        except AssertionError as e:
            print(f"Error: {e}")
            print("Please try again!\n")
            
    

    














# Main function
def main():
    """
    Main function to display menu and handle user inputs
    """

    while True:
    
        print("\n********** STUDENT INFORMATION & GRADE PROCESSING SYSTEM **********\n")

        print("1. Add Student Record")
        print("2. View All Student Information")
        print("3. Search Student by ID")
        print("4. Class Statistics")
        print("5. Update Student Marks")
        print("6. Delete Student Record")
        print("7. Exit")
        
        # Main loop
        try:
            choice = input("\nEnter your choice (1-7): ").strip()
                
            if choice == '1':
                add_student()
            elif choice == '2':
                view_all_students()
            elif choice == '3':
                search_student()
            elif choice == '5':
                update_student()
            elif choice == '7':
                print("\nExiting System...")
                print("Exited successfully!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 7.")

            """
            elif choice == '4':
                #calculate_statistics()
            elif choice == '5':
                #update_student()
            elif choice == '6':
                #delete_student()
            """
                  
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
        