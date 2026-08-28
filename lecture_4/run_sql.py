import sqlite3
conn = sqlite3.connect("school.db")

cursor = conn.cursor()

with open("query.sql", "r") as file:
    sql_script = file.read()

cursor.executescript(sql_script)

conn.commit()

conn.execute("Select students.full_name, grades.subject, grades.grade from grades JOIN students ON grades.student_id = students.id where students.full_name = 'Alice Johnson';")
conn.commit()
conn.close()

print("Database 'school.db' created successfully! ")