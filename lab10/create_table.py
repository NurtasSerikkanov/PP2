import psycopg2
from config import params

db=psycopg2.connect(**params)

current=db.cursor()

sql="""
    CREATE TABLE PhoneBook(
        person_name VARCHAR,
        phone_number VARCHAR,
        city VARCHAR
    );
"""

current.execute(sql)

current.close()
db.commit()
db.close()