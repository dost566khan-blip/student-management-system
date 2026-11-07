from database import connect_db

conn = connect_db()
cur = conn.cursor()

print("Inserting Values....")

cur.execute("""
    insert into students(name,email,age,city)
    values (%s, %s, %s, %s)
    returning*;
    """,("hammad","hammad12@gmail.com",25,"islamabad")
            
)
student=cur.fetchone()
conn.commit()

print("Student Added Successfully..")
print("student details",student)

cur.close()
conn.close()