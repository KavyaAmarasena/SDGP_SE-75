CREATE TABLE USERS 
(
	user_id VARCHAR(8),
    user_email VARCHAR(30),
    user_name VARCHAR(30),
    password VARCHAR(150),
    user_type VARCHAR(10) NOT NULL,
	constraint user_id_pk PRIMARY KEY(user_id)
);

SELECT * FROM USERS;

INSERT INTO USERS
(user_id,user_email,user_name,password,user_type)
VALUES
("w1867047","dinithofficial01@gmail.com","Dinith Fernando","7d4e3eec80026719639ed4dba68916eb94c7a49a053e05c8f9578fe4e5a3d7ea","student")

DROP TABLE USERS;