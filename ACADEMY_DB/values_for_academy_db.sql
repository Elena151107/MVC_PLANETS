INSERT INTO departments (financing, name) VALUES (5000, 'World History');
INSERT INTO departments (financing, name) VALUES (10000, 'Philosophy');
INSERT INTO departments (financing, name) VALUES (20000, 'English Language');
INSERT INTO departments (financing, name) VALUES (7000, 'Korean Language');
INSERT INTO departments (financing, name) VALUES (30000, 'Python');
INSERT INTO departments (financing, name) VALUES (19000, 'UX Design');
INSERT INTO departments (financing, name) VALUES (37000, 'Business');
INSERT INTO departments (financing, name) VALUES (27000, 'Banking');


INSERT INTO faculties (dean, name) VALUES ('Doronin', 'Computer Science');
INSERT INTO faculties (dean, name) VALUES ('Timofeeva', 'Economics and Business');
INSERT INTO faculties (dean, name) VALUES ('Kirova', 'Faculty of History');
INSERT INTO faculties (dean, name) VALUES ('Ivanov', 'Foreign Languages');


INSERT INTO groups (name, rating, year) VALUES ('history 1', 5, 3);
INSERT INTO groups (name, rating, year) VALUES ('history 2', 4, 1);
INSERT INTO groups (name, rating, year) VALUES ('python 1',5, 5);
INSERT INTO groups (name, rating, year) VALUES ('python 2',3, 2);
INSERT INTO groups (name, rating, year) VALUES ('banking 3',4, 1);


INSERT INTO teachers (employment_date, is_assistant, is_professor, name, position, premium, salary, surname) VALUES ('2019.02.13', TRUE, FALSE, 'Ivan', 'Преподаватель Корейского языка', 100, 900, 'Surin');
INSERT INTO teachers (employment_date, is_assistant, is_professor, name, position, premium, salary, surname) VALUES ('2020.12.01', TRUE, FALSE, 'Oleg', 'Преподаватель Python', 500, 1020, 'Utin');
INSERT INTO teachers (employment_date, is_assistant, is_professor, name, position, premium, salary, surname) VALUES ('2022.11.03', TRUE, FALSE, 'Maria', 'Преподаватель World history', 350, 950, 'Somova');

INSERT INTO teachers (employment_date, is_assistant, is_professor, name, position, premium, salary, surname) VALUES ('1999.11.03', FALSE, TRUE, 'Marina', 'Преподаватель World history', 700, 2000, 'Kirova');
INSERT INTO teachers (employment_date, is_assistant, is_professor, name, position, premium, salary, surname) VALUES ('2023.12.04', FALSE, TRUE, 'Olga', 'Преподаватель Python', 700, 1100, 'Utkina');
INSERT INTO teachers (employment_date, is_assistant, is_professor, name, position, premium, salary, surname) VALUES ('2024.07.25', FALSE, TRUE, 'Anton', 'Преподаватель Banking', 500, 1000, 'Larin');
INSERT INTO teachers (employment_date, is_assistant, is_professor, name, position, premium, salary, surname) VALUES ('2010.06.24', FALSE, TRUE, 'Semen', 'Преподаватель Business', 450, 1600, 'Minin');
