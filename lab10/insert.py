from pkg_resources import cleanup_resources
import psycopg2, csv
from config import params

db=psycopg2.connect(**params)

current=db.cursor()

sql="""
    INSERT INTO PhoneBook VALUES(%s, %s, %s) returning *;
"""
try:
    result=[]
    with open('PhoneBook.csv', 'r') as f:
        reader=csv.reader(f, delimiter=',')
        for row in reader:
            current.execute(sql, row)
            result.append(current.fetchone())
        print(result)

except Exception as e:
    name=input("Enter the name:")
    phone_number=input("Enter the phone_number:")
    city=input("Enter the city:")
    current.execute(sql, (name, phone_number, city))
    print(current.fetchone())

current.close()
db.commit()
db.close()