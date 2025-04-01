# Overview

As a software engineer, my goal is to deepen my understanding of relational databases and how to interact with them using SQL. By building a software program that interacts with a relational database, I aimed to learn how to structure, manage, and manipulate data effectively. This project required me to create a database, develop a series of functions to interact with it (such as adding, modifying, and deleting records), and explore the power of SQL commands in a real-world scenario.

The software I developed manages student records and course enrollments. The program uses a relational database (SQLite) to store, retrieve, and modify student and course data. It allows users to add new students, assign them to courses, update grades, and view the records stored in the database. The program integrates SQL queries to interact with the database, ensuring that each action (like adding or deleting data) is handled securely and efficiently.

To use the program, users can add student information, enroll students in courses, and update or delete records via simple function calls. The system ensures that data is stored consistently and that relationships between students and courses are maintained through foreign keys.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

The relational database ai created uses SQLite to store and manage student records and course enrollments. It allowed easy access without any complex setups. I made it have 2 main tables: students and courses. The students table included id, name, age, grade, and enrollment date. The courses table had course id, student is, and course name. 

# Development Environment

For this project I used Python as the main programming language. I was able to import the library sqlite3 to use the SQLite database. I also used the sqlite3 extension to be able to view the student database

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [SQLite](https://www.sqlite.org/docs.html)
- [sqlite3 — DB-API 2.0 interface for SQLite databases¶
](https://docs.python.org/3/library/sqlite3.html)
- [W3Schools](https://www.w3schools.com/sql/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Implementing a User Interface since the program mainly operates in a command line
- Add error handling
- Make it to where the students can enroll in multiple coourses