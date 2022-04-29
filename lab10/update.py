import psycopg2
from config import params

db=psycopg2.connect(**params)

current=db.cursor()

sql="""
    UPDATE PhoneBook SET phone_number=%s, person_name=%s;
"""
name=input()
phone_number=input()

current.execute(sql, (phone_number, name))

current.close()
db.commit()
db.close()