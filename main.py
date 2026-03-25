import sqlite3

conn = sqlite3.connect('registration.sqlite')
cur = conn.cursor()

choice = ""

while choice != "QUIT":

    print("\n1 Faculty")
    print("2 Course")
    print("3 Section")
    print("4 Student")
    print("5 Enrollment")
    print("6 Transcript")
    print("QUIT to exit")

    choice = input("Choice: ")

    #Faculty
    if choice == "1":
        action = input("1 list, 2 add, 3 update: ")

        if action == "1":
            cur.execute("SELECT * FROM Faculty")
            for row in cur:
                print(row)

        if action == "2":
            name = input("name ")
            email = input("email ")
            cur.execute("INSERT INTO Faculty (Name, Email) VALUES (?, ?)", (name, email))
            conn.commit()

        if action == "3":
            fid = int(input("id "))
            name = input("name ")
            email = input("email ")
            cur.execute("UPDATE Faculty SET Name=?, Email=? WHERE ID=?", (name, email, fid))
            conn.commit()

    #Course
    if choice == "2":
        action = input("1 list, 2 add, 3 update: ")

        if action == "1":
            cur.execute("SELECT * FROM Course")
            for row in cur:
                print(row)

        if action == "2":
            d = input("dept ")
            n = input("number ")
            c = int(input("credits "))
            desc = input("desc ")
            cur.execute("INSERT INTO Course (Department, Number, Credits, Description) VALUES (?, ?, ?, ?)", (d, n, c, desc))
            conn.commit()

        if action == "3":
            cid = int(input("id "))
            d = input("dept ")
            n = input("number ")
            c = int(input("credits "))
            desc = input("desc ")
            cur.execute("UPDATE Course SET Department=?, Number=?, Credits=?, Description=? WHERE ID=?", (d, n, c, desc, cid))
            conn.commit()

    #Section
    if choice == "3":
        action = input("1 list, 2 add, 3 update: ")

        if action == "1":
            cur.execute("SELECT * FROM Section")
            for row in cur:
                print(row)

        if action == "2":
            cid = int(input("course id "))
            fid = int(input("faculty id "))
            sem = input("semester ")
            day = input("day ")
            time = input("time ")
            cur.execute("INSERT INTO Section (Course_ID, Faculty_ID, Semester, Day, Time) VALUES (?, ?, ?, ?, ?)", (cid, fid, sem, day, time))
            conn.commit()

        if action == "3":
            sid = int(input("section id "))
            cid = int(input("course id "))
            fid = int(input("faculty id "))
            sem = input("semester ")
            day = input("day ")
            time = input("time ")
            cur.execute("UPDATE Section SET Course_ID=?, Faculty_ID=?, Semester=?, Day=?, Time=? WHERE ID=?", (cid, fid, sem, day, time, sid))
            conn.commit()

    #Student
    if choice == "4":
        action = input("1 list, 2 add, 3 update: ")

        if action == "1":
            cur.execute("SELECT * FROM Student")
            for row in cur:
                print(row)

        if action == "2":
            name = input("name ")
            major = input("major ")
            cur.execute("INSERT INTO Student (Name, Major) VALUES (?, ?)", (name, major))
            conn.commit()

        if action == "3":
            sid = int(input("id "))
            name = input("name ")
            major = input("major ")
            cur.execute("UPDATE Student SET Name=?, Major=? WHERE ID=?", (name, major, sid))
            conn.commit()

    #Enrollment
    if choice == "5":
        action = input("1 list, 2 add, 3 update, 4 delete: ")

        if action == "1":
            cur.execute("SELECT * FROM Enrollment")
            for row in cur:
                print(row)

        if action == "2":
            sid = int(input("student id "))
            sec = int(input("section id "))
            grade = int(input("grade "))
            cur.execute("INSERT INTO Enrollment (Student_ID, Section_ID, Grade) VALUES (?, ?, ?)", (sid, sec, grade))
            conn.commit()

        if action == "3":
            eid = int(input("id "))
            grade = int(input("new grade "))
            cur.execute("UPDATE Enrollment SET Grade=? WHERE ID=?", (grade, eid))
            conn.commit()

        if action == "4":
            eid = int(input("id "))
            cur.execute("DELETE FROM Enrollment WHERE ID=?", (eid,))
            conn.commit()

    #Transcript
    if choice == "6":
        sid = int(input("student id "))

        cur.execute("""
        SELECT Course.Department, Course.Number, Course.Credits, Enrollment.Grade
        FROM Enrollment
        INNER JOIN Student ON Student.ID = Enrollment.Student_ID
        INNER JOIN Section ON Section.ID = Enrollment.Section_ID
        INNER JOIN Course ON Course.ID = Section.Course_ID
        WHERE Student.ID = ?
        """, (sid,))

        print("transcript")
        for row in cur:
            print(row)

conn.close()