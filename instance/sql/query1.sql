SELECT * FROM teacher;

INSERT INTO Student
(std_id,std_fname,std_lname,std_email,std_pass)
VALUES
("w1867047","Dinith","Fernando","dinithofficial01@gmail.com","Dinith20010620")

SELECT * FROM student;

INSERT INTO Teacher
(tchr_id,tchr_fname,tchr_lname,tchr_email,tchr_pass)
VALUES
('w1526023t','Saman','Hettiarachchi','saman.h@gmail.com','pbkdf2:sha256:260000$1efPkGAzUZWJfrfm$6bcd7bef8cec826eb39a4e890c78a2a3d0076376bcab06a931d5517ba250712d')

SELECT * FROM teacher;

UPDATE Student 
SET std_pass = 'pbkdf2:sha256:260000$Z2wxxfx8m7xvRWBJ$a67fff574b51ccd3e037f783ad8d8e2f091638d96890332f062cf258e51edfe8'
WHERE std_id = "w1867047"

INSERT INTO Student
(std_id,std_fname,std_lname,std_email,std_pass)
VALUES
("w1870545","Indumini","Amarasena","indumini.a@gmail.com","pbkdf2:sha256:260000$ERgzbl7pQCcOgsB3$9e476cfb4156cd258426e384a00fcdd37f9565a740b34851fb103046f7cde78c")