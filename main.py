
from database import get_connection
from student import update_student_age, delete_student, search_student

import inspect

print("FILE:", inspect.getfile(search_student))
print("SIGNATURE:", inspect.signature(search_student))
print("ARGUMENT COUNT:", search_student.__code__.co_argcount)
def add_student():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Enter Student Name: ")
    email = input("Enter Student Email: ")
    age = get_valid_age()
    city = input("Enter Student City: ")
    
    cur.execute("""
        INSERT INTO students(name, email, age, city)
        VALUES (%s, %s, %s, %s)
        RETURNING *;
    """, (name, email, age, city))

    student = cur.fetchone()
    conn.commit()

    print("Student Added Successfully!")
    print("Student details:", student)

    cur.close()
    conn.close()
def get_valid_age():

    while True:
        try:
            age = int(input("Enter Student Age: "))

            if age > 0:
                return age

            else:
                print("Age must be greater than zero!")

        except ValueError:
            print("Please enter a valid number!")    


def display_students():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students ORDER BY student_id")
    students = cur.fetchall()

    if students:
        print("\n----- Student Records -----")
        for student in students:
            print(student)
    else:
        print("No student records found.")

    cur.close()
    conn.close()


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student Age")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            student_id = int(input("Enter Student ID: "))
            new_age = int(input("Enter New Age: "))
            update_student_age(student_id, new_age)

        elif choice == "4":
            student_id = int(input("Enter Student ID: "))
            delete_student(student_id)

        elif choice == "5":
            search_student()

        elif choice == "6":
            break


if __name__ == "__main__":
    main()
