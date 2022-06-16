import sqlite3

conn = sqlite3.connect("AWS-Women.db")

# Create a cursor
cursor = conn.cursor()

cursor.execute(""" INSERT INTO customers
                VALUES ('Jhon', 'Elder', 'john@example.com')
                """)

conn.commit()
conn.close()