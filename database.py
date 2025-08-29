import sqlite3
def init_db():
    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()
    
def register_student(name,email):
    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()
    cursor.execute('''INSERT INTO students(name,email) VALUES
                (?,?)''',(name,email))
    conn.commit()
    conn.close()