import psycopg2
from config import params

db=psycopg2.connect(**params)

current=db.cursor()

sql="""
    CREATE TABLE user_snake(
        user_name VARCHAR,
        highscore INT DEFAULT(0),
        score INT DEFAULT(0),
        level INT DEFAULT(0)
    );
"""

current.execute(sql)

current.close()
db.commit()
db.close()