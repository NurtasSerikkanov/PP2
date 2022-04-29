import psycopg2
from config import params

db=psycopg2.connect(**params)

current=db.cursor()

sql="""
    SELECT * FROM PhoneBook;
"""

current.execute(sql)

result=current.fetchall()

print(result)

current.close()
db.commit()
db.close()