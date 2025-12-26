# Student Information & Grade Processing System
# Included helper functions and custom exceptions:
    # 1. FileManager: Custom context manager for file handling
    # 2. read_students_file: Read file content(student records) using custom context manager
    # 3. validate_student_id: Validate the student ID format using using assert statements
    # 4. DuplicateIDError: Custom exception for duplicate student IDs
    # 5. check_duplicate_id: Check if student ID already exists in file
    # 6. validate_student_name: Validate the student name using using assert statements
    # 7. InvalidMarkError: Custom exception for invalid marks
    # 8. validate_marks: Validate the marks using custom exception: InvalidMarkError
    # 9. write_students_file: Write student records to file using custom context manager
    # 10. write_all_students_file: Write all student records to file using custom context manager
    # 11. calculate_grade: Calculate grade based on the stored marks
    # 12. calculate_total: Calculate total marks
    # 13. calculate_average: Calculate average marks
    # 14. display_student_table_header: Display the table header for student records
    # 15. display_student_row: Display a single student record in table format
    # 16. display_student_table_footer: Display the table footer (bottom border)


import csv

# Custom context manager
class FileManager:
    """
    Custom context manager for file handling
    """

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, newline="")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# Function to read file content using custom context manager
def read_students_file(filename):
    """
    Read file content(student records) using custom context manager
    """

    students =[]

    try:
        with FileManager(filename, 'r') as file:
            reader = csv.reader(file)

            # Skip header row
            next(reader, None)

            for row in reader:

                students.append({
                    "Student_ID": row[0],
                    "Student_Name": row[1],
                    "Science": int(row[2]),
                    "Maths": int(row[3])

                })
                            
    except (ValueError, IndexError):
        print("Error: Corrupted data in student records file.")

    return students


# Function to validate student ID
def validate_student_id(std_id):
    """
    Validate the student ID format using using assert statements
    """

    assert (std_id.startswith("S") or std_id.startswith("s")) and std_id[1:].isdigit(), "Invalid student ID format. Expected format: S001, S002, etc."

    assert std_id.strip() != "", "Student ID cannot be empty."

    assert isinstance(std_id, str) and len(std_id) == 4, "Invalid student ID format. Expected format: S001, S002, etc."


# Custom exception for duplicate student IDs
class DuplicateIDError(Exception):
    """
    Custom exception for duplicate student IDs
    """

    def __init__(self, std_id):
        self.std_id = std_id
        self.message = f"Duplicate student ID found: {std_id}. Please enter a unique ID.\n"
        super().__init__(self.message)


# Function to check if student ID already exists - Prevent duplicate student IDs
def check_duplicate_id(std_id, filename='students.txt'):
    """
    Check if student ID already exists in file
    """

    try:
        students = read_students_file(filename)

        for student in students:
            if student['Student_ID'] == std_id:
                return True

    except:
        pass

    return False


# Function to validate student name
def validate_student_name(std_name):
    """
    Validate the student name using using assert statements
    """

    assert isinstance(std_name, str) and std_name.strip() != "", "Student name cannot be empty"


# Custom exception for invalid marks
class InvalidMarkError(Exception):
    """
    Custom exception for invalid marks
    """

    def __init__(self, message):
        super().__init__(message) 
        self.message = message


# Function to validate marks
def validate_marks(mark):
    """
    Validate the marks using custom exception: InvalidMarkError
    (marks must be integers between 0-100)
    """

    try:
        assert 0 <= mark <= 100

    except AssertionError:
        raise InvalidMarkError("Invalid mark. Marks should be integers between 0 and 100.")
    

# Function to write student records to file
def write_students_file (filename, students):
    """
    Write(append) student records to file using custom context manager
    """

    # Check if file exists and has content
    file_is_empty = True
    try:
        with FileManager(filename, 'r') as file:
            f_line = file.readline()

            if f_line.strip():
                file_is_empty = False
        
    except FileNotFoundError:
        file_is_empty = True
    
    with FileManager(filename, 'a') as file:
        writer = csv.writer(file)

        # Write header row if file is empty
        if file_is_empty:
            writer.writerow(['Student_ID', 'Student_Name', 'Science', 'Maths'])

        for student in students:
            writer.writerow([student['Student_ID'], student['Student_Name'], student['Science'], student['Maths']])


# Function to write all student records to file
def write_all_students_file(filename, students):
    """
    Write all student records to file using custom context manager
    """
    
    with FileManager(filename, 'w') as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(['Student_ID', 'Student_Name', 'Science', 'Maths'])

        for student in students:
            writer.writerow([student['Student_ID'], student['Student_Name'], student['Science'], student['Maths']])


# Function to calculate grade
def calculate_grade(marks):
    """
    Calculate grade based on the stored marks
    Grades (A, B, C, D, or F)
    """

    if marks >= 90:
        return 'A+'
    elif marks >= 75:
        return 'A'
    elif marks >= 65:
        return 'B'
    elif marks >= 55:
        return 'C'
    elif marks >= 45:
        return 'S'
    else:
        return 'F'


# Function to calculate total marks
def calculate_total(marks):
    """
    Calculate total marks
    """

    return sum(marks)


# Function to calculate average marks
def calculate_average(marks, index=0, total=0):
    """
    Recursive function to calculate average marks
    """

    # Base case: reached end of list
    if index == len(marks):
        if len(marks) == 0:
            return 0
        return total / len(marks)
   
    # Recursive case: add current mark and move to next
    return calculate_average(marks, index + 1, total + marks[index])


# Function to display table header
def display_student_table_header():
    """
    Display the table header for student records
    """

    print("-" * 98)
    print(f"| {'Student ID':<12} | {'Student Name':<20} | {'Science':<10} | {'Maths':<10} | {'Total':<8} | {'Average':<10} | {'Grade':<6} |")
    print("-" * 98)


# Function to display a single student record row
def display_student_row(student):
    """
    Display a single student record in table format
    """

    # Calculate total, average, and grade
    total = calculate_total([student['Science'], student['Maths']])
    average = calculate_average([student['Science'], student['Maths']])
    grade = calculate_grade(average)
    
    # Print formatted row
    print(f"| {student['Student_ID']:<12} | {student['Student_Name']:<20} | {student['Science']:<10} | {student['Maths']:<10} | {total:<8} | {average:<10.2f} | {grade:<6} |")


# Function to display table footer
def display_student_table_footer():
    """
    Display the table footer (bottom border)
    """

    print("-" * 98)