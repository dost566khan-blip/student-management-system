from database import get_connection

def update_student_age(student_id,new_age):
    conn=get_connection()
    cursor=conn.cursor()

    query="""
       update students
       set age = %s
       where student_id = %s
"""
    cursor.execute(query,(new_age,student_id))

    if cursor.rowcount>0:
        conn.commit()
        print("Student Record Updated Successfully")
    else:
        print("student id not found")

    cursor.close()               
    conn.close()

student_id = int(input("Enter Student id:"))
new_age = int(input("Enter Student Age:"))

update_student_age(student_id,new_age)