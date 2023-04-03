SELECT * FROM teacher;

INSERT INTO Student
(std_id,std_fname,std_lname,std_email,std_pass)
VALUES
("w1867047","Dinith","Fernando","dinithofficial01@gmail.com","Dinith20010620")

SELECT * FROM student;

UPDATE Student 
SET std_pass = 'pbkdf2:sha256:260000$Z2wxxfx8m7xvRWBJ$a67fff574b51ccd3e037f783ad8d8e2f091638d96890332f062cf258e51edfe8'
WHERE std_id = "w1867047"