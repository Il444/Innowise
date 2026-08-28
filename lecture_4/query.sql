CREATE TABLE students(id integer PRIMARY KEY, full_name TEXT, birth_year integer);

INSERT INTO students(full_name, birth_year) VALUES("Alice Johnson", 2005);
INSERT INTO students(full_name, birth_year) VALUES("Brian Smith", 2004);
INSERT INTO students(full_name, birth_year) VALUES("Carla Reyes", 2006);
INSERT INTO students(full_name, birth_year) VALUES("Daniel Kim", 2005);
INSERT INTO students(full_name, birth_year) VALUES("Eva Thompson", 2003);
INSERT INTO students(full_name, birth_year) VALUES("Felix Nguyen", 2007);
INSERT INTO students(full_name, birth_year) VALUES("Grace Patel", 2005);
INSERT INTO students(full_name, birth_year) VALUES("Henry Lopez", 2004);
INSERT INTO students(full_name, birth_year) VALUES("Isabella Martinez", 2006);

CREATE TABLE grades(id integer PRIMARY KEY, student_id integer, subject TEXT, grade integer);

INSERT INTO grades(student_id, subject, grade) VALUES(1, "Math", 88);
INSERT INTO grades(student_id, subject, grade) VALUES(1, "English", 92);
INSERT INTO grades(student_id, subject, grade) VALUES(1, "Science", 85);
INSERT INTO grades(student_id, subject, grade) VALUES(2, "Math", 75);
INSERT INTO grades(student_id, subject, grade) VALUES(2, "History", 83);
INSERT INTO grades(student_id, subject, grade) VALUES(2, "English", 79);
INSERT INTO grades(student_id, subject, grade) VALUES(3, "Science", 95);
INSERT INTO grades(student_id, subject, grade) VALUES(3, "Math", 91);
INSERT INTO grades(student_id, subject, grade) VALUES(3, "Art", 89);
INSERT INTO grades(student_id, subject, grade) VALUES(4, "Math", 84);
INSERT INTO grades(student_id, subject, grade) VALUES(4, "Science", 88);
INSERT INTO grades(student_id, subject, grade) VALUES(4, "Physical education", 93);
INSERT INTO grades(student_id, subject, grade) VALUES(5, "English", 90);
INSERT INTO grades(student_id, subject, grade) VALUES(5, "History", 85);
INSERT INTO grades(student_id, subject, grade) VALUES(5, "Math", 88);
INSERT INTO grades(student_id, subject, grade) VALUES(6, "Science", 72);
INSERT INTO grades(student_id, subject, grade) VALUES(6, "Math", 78);
INSERT INTO grades(student_id, subject, grade) VALUES(6, "English", 81);
INSERT INTO grades(student_id, subject, grade) VALUES(7, "Art", 94);
INSERT INTO grades(student_id, subject, grade) VALUES(7, "Science", 87);
INSERT INTO grades(student_id, subject, grade) VALUES(7, "Math", 90);
INSERT INTO grades(student_id, subject, grade) VALUES(8, "History", 77);
INSERT INTO grades(student_id, subject, grade) VALUES(8, "Math", 83);
INSERT INTO grades(student_id, subject, grade) VALUES(8, "Science", 80);
INSERT INTO grades(student_id, subject, grade) VALUES(9, "English", 96);
INSERT INTO grades(student_id, subject, grade) VALUES(9, "Math", 89);
INSERT INTO grades(student_id, subject, grade) VALUES(9, "Art", 92);

Select * from students;

Select students.full_name, grades.subject, grades.grade from grades JOIN students ON grades.student_id = students.id where students.full_name = "Alice Johnson";