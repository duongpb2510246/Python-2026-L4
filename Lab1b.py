students = []
courses = []
marks = {}

def inputstudents():
    n = int(input("Numbers of students:"))
    for i in range (n):
        print(f"\n Student {i + 1}:")
        stid = input("Student ID:")
        stuname = input("Student name:")
        dob = input("Date of birth:")

        stu = {"id": stid, "name": stuname, "dob": dob}
        students.append(stu)

def inputcourses():
    n = int(input("\n Numbers of courses:"))
    for i in range(n):
        print(f"\nCourses {i + 1}:")
        coid = input("Courses ID:")
        coname = input("Courses name:")

        cors = {"id": coid, "name": coname}
        courses.append(cors)

def inputmarks():
    print("\n****INPUT MARKS****")
    coid = input("Input courses ID:")
    marks[coid] = {}
    for stu in students:
        mark = float(input(f"Input marks for students{stu['name']} (ID: {stu['id']}) "))
        marks[coid][stu["id"]] = mark

def liststudents():
    print("\n**** LIST STUDENTS ****")
    if not students:
        print ("No students available")
        return
    for stu in students:
        print(f"ID:{stu['id']} | Name: {stu['name']} | DoB: {stu['dob']}")

def listcourses():
    print("\n**** LIST COURSES ****")
    if not courses:
        print("No courses available")
        return
    for cors in courses:
        print(f"ID: {cors['id']} | Name: {cors['name']}")

def showstudentmarks():
    print("\n**** SHOW STUDENT MARKS ****")
    coid = input("Input course ID to show marks:")

    print(f"\n Marks for course {coid}:")
    course_marks = marks[coid]

    for stu in students:
        stuid = stu["id"]
        course_marks = marks[coid]
        print(f"ID: {stuid} | Name: {stu['name']} | Mark: {marks}")

    
        
def main():
    inputcourses()
    inputstudents()
    while True:
        print("\n================================")
        print(" STUDENT MANAGEMENT SYSTEM ")
        print("1.List courses")
        print("2.List students")
        print("3.Input Marks for a Courses")
        print("4.Show Student Marks for a Courses")
        print("5.Exit")

        choose = input("Select an option (1-5):")

        if choose == '1':
            listcourses()
        elif choose == '2':
            liststudents()
        elif choose == '3':
            inputmarks()
        elif choose == '4':
            showstudentmarks()
        elif choose == '5':
            print("Exiting")
            break
        else:
            print("Can not choose")


if __name__ == "__main__":
    main()
