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

INSERT INTO Student
(std_id,std_fname,std_lname,std_email,std_pass)
VALUES
("20210493","Hasini","Palihakkara","hasini.p@gmail.com","pbkdf2:sha256:260000$u3Wrcn6c4ZnqeGbA$bc68da9200ef3a780c7834a95379b410678bf9908ee085d32f72145b0d686bbb"),
("20210641","Salika","Hansani","salika.h@gmail.com","pbkdf2:sha256:260000$ZHBCii0vuhtQovWS$47470daeaf78115ed84116bb5395e81742807af01a569b1dd62fcf73484b9f87"),
("20210128","Theshan","Mahanayake","theshan.m@gmail.com","pbkdf2:sha256:260000$tUGtGJVjbokt4GOI$fd801ffb17c1fc364c7bc49bb4720631ccfa768c0998801f44e4cdedec55a5bc")

UPDATE Student
SET std_email = "dinith.f@gmail.com"
WHERE std_id = "w1867047";

CREATE TABLE Meetings(
    meeting_id VARCHAR(4),
    subject VARCHAR(30),
    teacher_id VARCHAR(10),
    CONSTRAINT pk_meeting_if PRIMARY KEY(meeting_id),
    CONSTRAINT fk_teacher_id FOREIGN KEY (teacher_id) REFERENCES Teacher(tchr_id)
);

DROP TABLE Meetings;

SELECT * FROM Meetings;

INSERT INTO Meetings
(meeting_id,subject,teacher_id)
VALUES
("M001","OOP","w1526023t");

CREATE TABLE Marks(
    mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
    std_id VARCHAR(10) NOT NULL,
    meeting_id VARCHAR(4) NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    marks int NOT NULL,
    CONSTRAINT fk_std_id FOREIGN KEY(std_id) REFERENCES student(std_id),
    CONSTRAINT fk_meeting_id FOREIGN KEY(meeting_id) REFERENCES meetings(meeting_id)
);

INSERT INTO Marks
(std_id,meeting_id,date,time,marks)
VALUES
("w1867047","M001",CURRENT_DATE,CURRENT_TIME,20)

SELECT * FROM Marks;

SELECT marks.std_id,student.std_fname,student.std_lname,SUM(marks) as total_marks
FROM Marks marks JOIN Student student
ON marks.std_id = student.std_id
WHERE date = '2023-04-05'
GROUP BY marks.std_id;