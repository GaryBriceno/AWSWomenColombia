# SQLite come with Python
import sqlite3

# Si quiero utilizar la BD en memoria
conn = sqlite3.connect(":memory:")

# connection to database
# Si no existe, lo genera
conn = sqlite3.connect(database="AWS-Women.db")


# Creacion de una Tabla
# Para comunicarnos con la base de datos, utilizamos un objeto Cursor

cursor = conn.cursor()
# Utilizar docstring para enviar los comandos
cursor.execute("""CREATE TABLE customers 
               (first_name TEXT, 
               last_name TEXT, 
               email TEXT)""")

# Utiliza SQL para el envio de los comandos
# Data Types: NULL, INTEGER, REAL, TEXT, BLOB

# Execute the sentences in the database
conn.commit()

# Close the connection
conn.close()
