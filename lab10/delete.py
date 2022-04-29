import psycopg2
from config import params

db=psycopg2.connect(**params)

current=db.cursor()

sql="""
    DELETE FROM PhoneBook WHERE person_name=%s;
"""
name=input()

current.execute(sql, (name,))

current.close()
db.commit()
db.close()