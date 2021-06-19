import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="learning")
cur = con.cursor(buffered=True)

def Add_Student():
    Name = str (input("Enter student Name: "))
    School_name = str(input("Enter School Name: "))
    Tamil = int(input("Enter Tamil Mark: "))
    English= int(input("Enter English Mark: "))
    Maths = int(input("Enter Maths Mark: "))
    Science = int(input("Enter Science Mark: "))
    Social = int(input("Enter Social Mark: "))
    total = Tamil+English+Maths+Science+Social
    Avg = round(total/5)
    Grade = Grade_calc(Avg)

    cur.execute(
            """INSERT INTO school (Name, School_Name,Tamil,English,Maths,Science,Social,Total,Average,Grade) VALUES (\"""" + Name + """\",\"""" + School_name + """\",""" + str(
                Tamil) + """,""" + str(English) + """,""" + str(Maths) + """,""" + str(Science) + """,""" + str(
                Social) + """,""" + str(total) + """,""" + str(Avg) + """,\"""" + Grade + """\")""")
    con.commit()


def Grade_calc(Avg):
    if (Avg >= 0 and Avg < 30):
        Grade = 'C'
    elif (Avg > 30 and Avg < 60):
        Grade = 'B'
    elif (Avg >= 60 and Avg <= 100):
        Grade = 'A'
    else:
        print('Enter correct marks')
    return Grade

def find_student():
    new = str(input("enter the student name: "))
    cur.execute("""select * from school where Name =\""""+new+"""\";""")
    result = cur.fetchall()
    for i in result:
        print(i)

def get_all_student():
    cur.execute("select * from school")
    result = cur.fetchall()
    for i in result:
        print(i)

def delete_student():
    name3 = str(input("enter the student name: "))
    cur.execute("""DELETE FROM school WHERE Name= \"""" + name3 + """\";""")
    con.commit()
    print("student deleted successfully")

def update_student():
    name = str(input("enter the name: "))
    cur.execute("""select Name from school where Name =\"""" + name + """\";""")

    name1 = cur.fetchone()
    for i in name1:
        name2 = i

    def change_name():
        new_name = str(input("enter the new name: "))
        cur.execute("""UPDATE 
                           school
                       SET
                           Name = REPLACE(Name,\"""" + name + """\",\"""" + new_name + """\")
                       WHERE
                           Name IS NOT NULL;""")
        con.commit()
        print("changes completed")


    def change_schoolname():
        old_name = str(input("enter the old school name: "))
        new_name = str(input("enter the new school name: "))
        cur.execute("""UPDATE 
                            school
                       SET
                            School_Name = REPLACE(School_Name,\"""" + old_name + """\",\"""" + new_name + """\")
                       WHERE
                            School_Name IS NOT NULL;""")
        print("changes completed")
        con.commit()

    def change_mark(Subject):
        cur.execute("""select """+Subject+""" from school where Name =\"""" + name + """\";""")
        TamilMark = cur.fetchone()
        for i in TamilMark:
            tamilMark = i
        cur.execute("""select Total from school where Name =\"""" + name + """\";""")
        totalMark = cur.fetchone()
        for i in totalMark:
            totalMark = i

        old_grade = Grade_calc(totalMark/5)
        new_total = totalMark - tamilMark
        new1 = int(input("enter the new subject mark: "))
        new_total1 = new1 + new_total
        Avg = round(new_total1/5)
        new_grade = Grade_calc(Avg)
        cur.execute("""UPDATE
                            school
                       SET
                            """+Subject+""" = REPLACE("""+Subject+""",""" + str(tamilMark) + """,""" + str(new1) + """),
                            Total = REPLACE(Total,""" + str(totalMark) + """,""" + str(new_total1) + """),
                            Average = REPLACE(Average,""" + str(round(totalMark/5)) + """,""" + str(Avg) + """),
                            Grade = REPLACE(Grade,\"""" + old_grade + """\",\"""" + new_grade + """\")
                       WHERE
                            Name=\""""+name+"""\";""")
        con.commit()
        print("changes completed")

    while (True):

        if name2 != name:
            print("enter the valid name")
            break
        elif name2 == name:
            print("1. Change Name")
            print("2. Change SchoolNAme")
            print("3. Change Tamil Mark")
            print("4. change English Mark")
            print("5. change Maths Mark")
            print("6. change Science Mark")
            print("7. change Social Mark")
            print("8. Quit")
            b = int(input("enter the number: "))
            if b == 1:
                change_name()
            elif b == 2:
                change_schoolname()
            elif b == 3:
                change_mark("Tamil")
            elif b == 4:
                change_mark("English")
            elif b == 5:
                change_mark("Maths")
            elif b == 6:
                change_mark("Science")
            elif b == 7:
                change_mark("Social")
            elif b == 8:
                break
        else:
            break

while(True):
    print('Menu')
    print('1. Add Student')
    print('2. Get student')
    print('3. Get all student')
    print('4. Update student')
    print('5. Delete student')
    print('6. Exit')
    a = int(input("Enter the value: "))
    if a == 6:
        print(" ******** Thank you using our Application **********")
        break
    elif a == 1:
        Add_Student()
    elif a == 2:
        find_student()
    elif a == 3:
        get_all_student()
    elif a == 4:
        update_student()
    elif a == 5:
        delete_student()








