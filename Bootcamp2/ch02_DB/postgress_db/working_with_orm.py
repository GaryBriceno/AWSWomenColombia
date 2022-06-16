import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData

db_string = "postgresql+psycopg2://postgres:mypassword@localhost:5432/test"

db = create_engine(db_string)

meta = MetaData(db)

film_table = Table('films_orm', meta,
                   Column('title', String),
                   Column('director', String),
                   Column('year', String))

with db.connect() as conn:

    # Create
    try:
        film_table.create()
    except:
        pass

    insert_statement = film_table.insert().values(title="Doctor Strange",
                                                  director="Scott Derrickson",
                                                  year="2016")
    conn.execute(insert_statement)

    # Read
    select_statement = film_table.select()
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)

    # Update
    update_statement = film_table.update().where(film_table.c.year == "2016").values(title="Some2016Film")
    conn.execute(update_statement)

    # Delete
    delete_statement = film_table.delete().where(film_table.c.year == "2016")
    conn.execute(delete_statement)