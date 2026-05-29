student={}
while True:
    print("-----student management system-----")
    print("1)add student")
    print("2)view student")    
    print("3)update student")
    print("4)delete student")  
    print("5)exit student")

    option=input("enter your option: ")
    if option=="1":
        roll_no=input("enter roll_number")
        if roll_no in student:
            print(f"student roll_no {roll_no} is already exits")
        else:
            student_name=input("enter name")
            student_age=input("enter age")
            student_marks=input("enter marks")
            student_grade=input("enter grade")
            student[roll_no]={"student_name":student_name,"student_age":student_age,"student_marks":student_marks,"student_grade":student_grade}
            print("student added")

    elif option=="2":
        roll_no=input("enter roll_no to view") 
        if roll_no in student:
            print("------student details------")
            for student_roll_no,details in student.items():      
             print(f"roll_no {roll_no}")
             print(f"name {student_name}")
             print(f"age {student_age}")
             print(f"marks {student_marks}")
             print(f"grade {student_grade}")
        else:
            print("student not found")
    elif option=="3":
        roll_no=input("enter roll_no to update")
        if roll_no in student:
            student_name=input("enter name")
            student_age=input("enter age")
            student_marks=input("enter marks")
            student_grade=input("enter grade")
            print("student updated")
        else:
            print("student not found")
    elif option=="4":
        roll_no=input("enter roll_no to delete")
        if roll_no in student:
            del student[roll_no]
            print("student deleted")
        else:
            print("student not found")
    elif option=="5":
        print("exit the student management")
    else:
        print("invali choice try agine in 1 to 5 option")
