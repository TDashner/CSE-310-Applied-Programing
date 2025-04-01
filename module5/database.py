import sqlite3

DATABASE_NAME = "students.db"

def connect_db():
    """Create a connection to the database."""
    return sqlite3.connect(DATABASE_NAME)

def setup_database():
    """Create necessary tables if they do not exist."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade REAL,
                enrollment_date TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                course_name TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
            )
        ''')

def add_student(name, age, grade, enrollment_date):
    """Insert a new student record."""
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, age, grade, enrollment_date) VALUES (?, ?, ?, ?)", 
                (name, age, grade, enrollment_date)
            )
            conn.commit()
            print(f"Student '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")

def get_students():
    """Retrieve all students from the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

def update_grade(student_id, new_grade):
    """Update a student's grade."""
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
            conn.commit()
            if cursor.rowcount:
                print(f"Updated student {student_id}'s grade to {new_grade}.")
            else:
                print("Student ID not found.")
    except sqlite3.Error as e:
        print(f"Error updating grade: {e}")

def delete_student(student_id):
    """Delete a student from the database."""
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()
            if cursor.rowcount:
                print(f"Deleted student with ID {student_id}.")
            else:
                print("Student ID not found.")
    except sqlite3.Error as e:
        print(f"Error deleting student: {e}")

def add_course(student_id, course_name):
    """Enroll a student in a course."""
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM students WHERE id = ?", (student_id,))
            if cursor.fetchone():
                cursor.execute("INSERT INTO courses (student_id, course_name) VALUES (?, ?)", (student_id, course_name))
                conn.commit()
                print(f"Student {student_id} enrolled in '{course_name}'.")
            else:
                print("Student ID does not exist.")
    except sqlite3.Error as e:
        print(f"Error enrolling student in course: {e}")

def get_students_with_courses():
    """Retrieve students along with their courses."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT students.name, courses.course_name
            FROM students
            JOIN courses ON students.id = courses.student_id
        ''')
        return cursor.fetchall()

# Run setup
setup_database()

# Example usage
add_student("Alice Johnson", 20, 85.5, "2024-03-25")
add_course(1, "Math 101")

# Display students
print("\nAll Students:")
for student in get_students():
    print(student)

# Display students with courses
print("\nStudents with Courses:")
for row in get_students_with_courses():
    print(row)

# Update student grade
update_grade(1, 90.2)

# Delete student
delete_student(1)


def get_average_grade():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT AVG(grade) FROM students")
        avg_grade = cursor.fetchone()[0]
        return avg_grade if avg_grade else "No students found."
print("Average Grade:", get_average_grade())

