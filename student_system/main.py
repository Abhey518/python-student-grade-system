# Student Information & Grade Processing System

# Assumptions:
    # 1. Student ID format: S001, S002, etc. (S followed by 3 digits)
    # 2. Only marks can be updated; to change ID/Name, delete and re add the record

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

    try:
        students = read_students_file(STUDENT_FILE)

    except FileNotFoundError:
        print("No student records file found. Please add students first.")
        print("Returning to main menu...")
        return

    # Check if there are any students
    if not students:
        print("No student records found.")
        print("Returning to main menu...\n")
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
            print("Returning to main menu...")
            return

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


# Function for Class Statistics
def class_statistics():
    """
    Calculate and display class statistics
    """

    print("\n---------- Class Statistics ----------\n")

    try:
        # Read all students
        students = read_students_file(STUDENT_FILE)

        # Check if file is empty
        if not students:
            print("No student records found.")
            return

        # Extract marks into lists
        science_marks = [student['Science'] for student in students]
        maths_marks = [student['Maths'] for student in students]

        # Calculate averages
        science_avg = calculate_average(science_marks)
        maths_avg = calculate_average(maths_marks)

        # Find highest marks
        highest_science_mark = max(science_marks)
        highest_science_students = [s for s in students if s['Science'] == highest_science_mark]
        highest_maths_mark = max(maths_marks)
        highest_maths_students = [s for s in students if s['Maths'] == highest_maths_mark]

        # Find lowest marks
        lowest_science_mark = min(science_marks)
        lowest_science_students = [s for s in students if s['Science'] == lowest_science_mark]
        lowest_maths_mark = min(maths_marks)
        lowest_maths_students = [s for s in students if s['Maths'] == lowest_maths_mark]

        # Display statistics
        print(f"Total Students: {len(students)}\n")
            
        print("SCIENCE STATISTICS:", end="")
        print("-" * 40 )
        print(f"  Average Marks: {science_avg:.2f}")
        print()

        print(f"  Highest: {highest_science_mark}", end="")

        if len(highest_science_students) > 1:
            print(f" (Tied - {len(highest_science_students)} students)")
            for student in highest_science_students:
                print(f"    - {student['Student_ID']} - {student['Student_Name']}")

        else:
            print(f"\n    - {highest_science_students[0]['Student_ID']} - {highest_science_students[0]['Student_Name']}")
        print()

        print(f"  Lowest: {lowest_science_mark}", end="")

        if len(lowest_science_students) > 1:
            print(f" (Tied - {len(lowest_science_students)} students)")
            for student in lowest_science_students:
                print(f"    - {student['Student_ID']} - {student['Student_Name']}")

        else:
            print(f"\n    - {lowest_science_students[0]['Student_ID']} - {lowest_science_students[0]['Student_Name']}")
            
        print("\nMATHS STATISTICS:", end="")
        print("-" * 42)
        print(f"  Average Marks: {maths_avg:.2f}")
        print()

        print(f"  Highest: {highest_maths_mark}", end="")

        if len(highest_maths_students) > 1:
            print(f" (Tied - {len(highest_maths_students)} students)")
            for student in highest_maths_students:
                print(f"    - {student['Student_ID']} - {student['Student_Name']}")

        else:
            print(f"\n    - {highest_maths_students[0]['Student_ID']} - {highest_maths_students[0]['Student_Name']}")
        print()

        print(f"  Lowest: {lowest_maths_mark}", end="")

        if len(lowest_maths_students) > 1:
            print(f" (Tied - {len(lowest_maths_students)} students)")
            for student in lowest_maths_students:
                print(f"    - {student['Student_ID']} - {student['Student_Name']}")

        else:
            print(f"\n    - {lowest_maths_students[0]['Student_ID']} - {lowest_maths_students[0]['Student_Name']}")

    except FileNotFoundError:
        print("No student records file found. Please add students first.")
        print("Returning to main menu...")
        return

    except Exception as e:
        print(f"Error calculating statistics: {e}")


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
            
            # Write updated records back to file
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
            print("Returning to main menu...")
            break
        
        except AssertionError as e:
            print(f"Error: {e}")
            print("Please try again!\n")
            

# Function for Delete Student Record
def delete_student():
    """
    Delete a student record using Student ID
    """

    print("\n---------- Delete Student Record ----------\n")

    while True:
        try:
            # Get student ID to delete
            std_id = input("Enter Student ID to delete: ").strip()
            
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
            
            # Ask user for confirmation
            confirm = input("Are you sure you want to delete this student record? (y/n): ").strip().lower()
            
            if confirm == 'y':
                # Delete the student record
                del students[f_index]
            
                # Write updated records back to file
                write_all_students_file(STUDENT_FILE, students)
                
                print("\nStudent record deleted successfully!")
                break
            
            elif confirm == 'n':
                print("Deletion cancelled successfully.")
                print("Returning to main menu...")
                return
            else:
                print("Invalid input. Returning to main menu...")
                return

        except FileNotFoundError:
            print("No student records file found. Please add students first.")
            print("Returning to main menu...")
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
            elif choice == '4':
                class_statistics()
            elif choice == '5':
                update_student()
            elif choice == '6':
                delete_student()
            elif choice == '7':
                print("\nExiting System...")
                print("System closed successfully!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 7.")

        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()