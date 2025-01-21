## Задание: Академия (Academy)

"""Необходимо создать базу данных, которая будет содержать информацию о сотрудниках и внутреннем устройстве академии.
Преподаватели, читающие лекции в академии представлены в виде таблицы  - Преподаватели (Teachers), в которой собрана основная информация, такая
как: имя, фамилия, данные о зарплате, а также дата приема на работу.
Также в базе данных присутствует информация о группах, хранимая в таблице - Группы (Groups).
Данные об факультетах и кафедрах содержатся в таблицах - Факультеты (Faculties), Кафедры (Departments) соответственно.
"""

import sqlite3

conn = sqlite3.connect('academy.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
id INTEGER PRIMARY KEY AUTOINCREMENT,
financing INTEGER NOT NULL CHECK(financing >= 0),
name TEXT NOT NULL UNIQUE
)
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS faculties (
id INTEGER PRIMARY KEY AUTOINCREMENT,
dean TEXT NOT NULL,
name TEXT NOT NULL UNIQUE
)
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS groups (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE,
rating INTEGER NOT NULL CHECK(rating BETWEEN 0 AND 5),
year INTEGER NOT NULL CHECK(year BETWEEN 1 AND 5)
)
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
employment_date DATE NOT NULL CHECK(employment_date >= '1990.01.01'),
is_assistant BOOLEAN NOT NULL,
is_professor BOOLEAN NOT NULL,
name TEXT NOT NULL,
position TEXT NOT NULL,
premium REAL NOT NULL CHECK(premium >= 0),
salary REAL NOT NULL CHECK(salary > 0),
surname TEXT NOT NULL
)
""")
conn.commit()

def insert_values_in_bd():
    with conn:
        cursor = conn.cursor()
        with open('values_for_academy_db.sql', 'r', encoding='utf-8') as file:
            cursor.executescript(file.read())


def main():
    with conn:
        cursor = conn.cursor()

        ## 1
        print('1. Вывести таблицу кафедр, но расположить ее поля в обратном порядке:')
        result = cursor.execute('''
        select name, financing, id from departments
        ''').fetchall()
        if result:
            for res in result:
                print(f'Name of departments: {res[0]}, financing: {res[1]}, id: {res[2]}')
        else:
            print('No departments')

        ## 2
        print()
        print('2. Вывести названия групп и их рейтинги с уточнением имен полей именем таблицы:')
        result = cursor.execute('''
        select name as GroupName, rating as GroupRating from groups
        ''').fetchall()
        if result:
            for res in result:
                print(f'GroupName: {res[0]}, GroupRating: {res[1]}')
        else:
            print('No groups')

        ## 3
        print()
        print('3. Вывести для преподавателей их фамилию, процент ставки по отношению к надбавке и процент ставки по отношению к зарплате (сумма ставки и надбавки):')
        result = cursor.execute('''
        select surname, round((premium * 100) / salary, 2) as 'Процент ставки к надбавке', round((salary * 100) / (salary + premium), 2) as 'Процент ставки к зарплате' from teachers
        ''').fetchall()
        if result:
            for res in result:
                print(f'Teacher: {res[0]}, Процент ставки к надбавке: {res[1]} %, Процент ставки к зарплате: {res[2]} %')
        else:
            print('No teachers')

        ## 4
        print()
        print('4. Вывести фамилии преподавателей, которые являются профессорами и ставка которых превышает 1050:')
        result = cursor.execute('''
        select surname from teachers
        where is_professor = 1 and salary > 1050
        ''').fetchall()
        if result:
            for res in result:
                print(f'Surname teachers: {res[0]}')
        else:
            print('No teachers')

        ## 5
        print()
        print('5. Вывести названия кафедр, фонд финансирования которых меньше 11 000 или больше 25 000:')
        result = cursor.execute('''
        select name from departments
        where financing < 11000 or financing > 25000
        ''').fetchall()
        if result:
            for res in result:
                print(f'Departments: {res[0]}')
        else:
            print('No departments')

        ## 6
        print()
        print('6. Вывести названия факультетов кроме факультета “Computer Science”:')
        result = cursor.execute('''
        select name from faculties
        where name is not 'Computer Science'
        ''').fetchall()
        if result:
            for res in result:
                print(f'Faculties: {res[0]}')
        else:
            print('No faculties')

        ## 7
        print()
        print('7. Вывести фамилии и должности преподавателей, которые не являются профессорами:')
        result = cursor.execute('''
        select surname, position from teachers
        where is_professor = 0
        ''').fetchall()
        if result:
            for res in result:
                print(f'Teachers: {res[0]}, position: {res[1]}')
        else:
            print('No teachers')

        ## 8
        print()
        print('8. Вывести фамилии, должности, ставки и надбавки ассистентов, у которых надбавка в диапазоне от 160 до 550:')
        result = cursor.execute('''
        select surname, position, salary, premium from teachers
        where is_professor = 0 and premium between 160 and 550
        ''').fetchall()
        if result:
            for res in result:
                print(f'Assistant: {res[0]}, position: {res[1]}, salary: {res[2]}, premium: {res[3]}')
        else:
            print('No assistants')

        ## 9
        print()
        print('9. Вывести фамилии и ставки ассистентов:')
        result = cursor.execute('''
        select surname, salary from teachers
        where is_assistant = 1
        ''').fetchall()
        if result:
            for res in result:
                print(f'Assistant: {res[0]}, salary: {res[1]}')
        else:
            print('No assistants')

        ## 10
        print()
        print('10. Вывести фамилии и должности преподавателей, которые были приняты на работу до 01.01.2000:')
        result = cursor.execute('''
        select surname, position from teachers
        where employment_date < '2020.01.01'
        ''').fetchall()
        if result:
            for res in result:
                print(f'Teacher: {res[0]}, position: {res[1]}')
        else:
            print('No teachers')

        ## 11
        print()
        print('11. Вывести фамилии ассистентов, имеющих зарплату (сумма ставки и надбавки) не более 1200:')
        result = cursor.execute('''
        select surname from teachers
        where is_assistant = 1 and (salary + premium) <= 1200
        ''').fetchall()
        if result:
            for res in result:
                print(f'Assistant: {res[0]}')
        else:
            print('No assistants')


# insert_values_in_bd()
main()
