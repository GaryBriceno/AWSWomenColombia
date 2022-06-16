from sqlalchemy import create_engine

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
db_string = "postgresql+psycopg2://postgres:mypassword@localhost:5432/test"

db = create_engine(db_string)

db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")
db.execute("INSERT INTO films (title, director, year) VALUES ('Titanic', 'Cameron Diaz', '1997')")

# Read
result_set = db.execute("SELECT * FROM films")
for r in result_set:
    print(r)

# Update
db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")

# Delete
db.execute("DELETE FROM films WHERE year='2016' ")
