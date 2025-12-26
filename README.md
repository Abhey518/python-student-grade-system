# Student Information & Grade Processing System

A comprehensive Python-based student management system for tracking student records, marks, and generating class statistics.

## Features

### Core Functionality

- ✅ **Add Student Records** - Register new students with ID, name, and marks
- ✅ **View All Students** - Display all student records in a formatted table
- ✅ **Search Student** - Find student records by ID
- ✅ **Class Statistics** - Generate comprehensive statistics with:
  - Recursive average calculation
  - Highest/lowest marks using lambda expressions
  - Tied marks handling (displays all students with same marks)
- ✅ **Update Student Marks** - Modify existing student marks
- ✅ **Delete Student Records** - Remove student records with confirmation

### Technical Features

- **Custom Context Manager** - `FileManager` for efficient file handling
- **Custom Exceptions** - `DuplicateIDError` and `InvalidMarkError` for robust error handling
- **Input Validation** - Comprehensive validation for student IDs, names, and marks
- **Recursive Functions** - Average calculation using recursion
- **Lambda Expressions** - Finding highest/lowest marks
- **CSV File Storage** - Persistent data storage using CSV format

## Project Structure

```
student_system/
├── main.py          # Main application with menu and CRUD operations
├── utils.py         # Utility functions, validators, and custom classes
└── students.txt     # CSV file for storing student records
```

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Abhey518/python-student-grade-system.git
   cd python-student-grade-system
   ```

2. **Navigate to the student_system directory**

   ```bash
   cd student_system
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## Usage

### Main Menu Options

```
1. Add Student Record
2. View All Student Information
3. Search Student by ID
4. Class Statistics
5. Update Student Marks
6. Delete Student Record
7. Exit
```

### Student ID Format

- Format: `S001`, `S002`, `S003`, etc.
- Must start with 'S' followed by 3 digits
- Case insensitive (accepts both `s001` and `S001`)

### Marks Range

- Valid range: 0-100 (integers only)
- Subjects: Science and Maths

### Grading System

- **A+**: 90-100
- **A**: 75-89
- **B**: 65-74
- **C**: 55-64
- **S**: 45-54
- **F**: Below 45

## Examples

### Adding a Student

```
Enter Student ID (format: S001): S001
Enter Student Name: Alice Johnson
Enter Science Marks (0-100): 85
Enter Maths Marks (0-100): 90
```

### Class Statistics Output

```
Total Students: 3

SCIENCE STATISTICS:
  Average Marks: 85.00
  Highest: 95
    - S003 - Charlie
  Lowest: 75
    - S002 - Bob

MATHS STATISTICS:
  Average Marks: 80.00
  Highest: 90 (Tied - 2 students)
    - S001 - Alice
    - S004 - David
  Lowest: 70
    - S003 - Charlie
```

## Input Validation

The system validates:

- ✅ Student ID format (S + 3 digits)
- ✅ Duplicate student IDs
- ✅ Empty student names
- ✅ Marks range (0-100)
- ✅ Integer marks only

## Error Handling

- **FileNotFoundError** - Handles missing student records file
- **DuplicateIDError** - Prevents duplicate student IDs
- **InvalidMarkError** - Validates marks range
- **AssertionError** - Catches validation failures
- **ValueError** - Handles non-integer mark inputs

## Assumptions

1. Student ID format: S001, S002, etc. (S followed by 3 digits)
2. Only marks can be updated; to change ID/Name, delete and re-add the record

## Technical Implementation

### Custom Context Manager

```python
class FileManager:
    """Custom context manager for file handling"""
    def __enter__(self):
        # Open file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Close file
```

### Recursive Average Calculation

```python
def calculate_average(marks, index=0, total=0):
    """Recursive function to calculate average marks"""
    if index == len(marks):
        return total / len(marks)
    return calculate_average(marks, index + 1, total + marks[index])
```

### Lambda Expressions for Statistics

```python
highest_science_mark = max(science_marks)
highest_science_students = [s for s in students if s['Science'] == highest_science_mark]
```

## File Format

Student records are stored in CSV format:

```csv
Student_ID,Student_Name,Science,Maths
S001,Alice Johnson,85,90
S002,Bob Smith,75,80
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Abhey**

- GitHub: [@Abhey518](https://github.com/Abhey518)

## Acknowledgments

This is an **individual academic project** developed as part of the coursework requirements.

- **Course**: CTEC 31042 - Python Programming
- **Semester**: V
- **Project Type**: Individual Mini Project

---

**Note**: This system is designed for educational purposes and demonstrates Python programming concepts including file I/O, custom exceptions, context managers, recursion, and lambda expressions.
