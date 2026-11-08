
from database import get_connection


def update_student_age(student_id, new_age):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE students
        SET age = %s
        WHERE student_id = %s
    """

    cursor.execute(query, (new_age, student_id))

    if cursor.rowcount > 0:
        conn.commit()
        print("Student Record Updated Successfully")
    else:
        print("Student ID not found")

    cursor.close()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        DELETE FROM students
        WHERE student_id = %s
    """

    cursor.execute(query, (student_id,))

    if cursor.rowcount > 0:
        conn.commit()
        print("Student deleted successfully")
    else:
        print("Student ID not found")

    cursor.close()
    conn.close()


# Testing DELETE
#student_id = int(input("Enter Student ID:"))
#delete_student(student_id)

# Testing UPDATE (uncomment when needed)
# student_id = int(input("Enter Student ID:"))
# new_age = int(input("Enter Student Age:"))
# update_student_age(student_id, new_age)
