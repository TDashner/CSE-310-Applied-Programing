import sqlite3

# Connect to SQLite (creates a file 'students.db' if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create a Students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade REAL,
        enrollment_date TEXT
    )
''')

conn.commit()
conn.close()


def add_student(name, age, grade, enrollment_date):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade, enrollment_date) VALUES (?, ?, ?, ?)", 
                   (name, age, grade, enrollment_date))
    conn.commit()
    conn.close()
add_student("Alice Johnson", 20, 85.5, "2024-03-25")

def get_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

# Display results
for student in get_students():
    print(student)

def update_grade(student_id, new_grade):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    conn.commit()
    conn.close()
update_grade(1, 90.2)

def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
delete_student(1)

def setup_courses_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    
    # Create Courses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_name TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    ''')
    
    conn.commit()
    conn.close()

def add_course(student_id, course_name):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (student_id, course_name) VALUES (?, ?)", 
                   (student_id, course_name))
    conn.commit()
    conn.close()

def get_students_with_courses():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT students.name, courses.course_name
        FROM students
        JOIN courses ON students.id = courses.student_id
    ''')
    results = cursor.fetchall()
    conn.close()
    return results

# Example usage
setup_courses_table()
add_course(1, "Math 101")
for row in get_students_with_courses():
    print(row)

