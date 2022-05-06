import psycopg2
from config import params

config = psycopg2.connect(**params)
current = config.cursor()

def checkNum(number):
    if(number.find('8707') == 0 and len(number) == 11):
        return number
    elif(number.find('8747') == 0 and len(number) == 11):
        return number
    elif(number.find('8775') == 0 and len(number) == 11):
        return number
    elif(number.find('8708') == 0 and len(number) == 11):
        return number
    elif(number.find('8777') == 0 and len(number) == 11):
        return number
    elif(number.find('8778') == 0 and len(number) == 11):
        return number
    elif(number.find('8700') == 0 and len(number) == 11):
        return number
    print("Sorry, it seems you made a mistake in your phone_number, can you write it again?")
    number = str(input())
    return checkNum(number)

def check(name):
    select = '''
            SELECT phone_number FROM PhoneBook WHERE person_name = %s;
    '''
    current.execute(select, [name])
    DICT = current.fetchone()
    if DICT == None: return True
    else: return False


print("What's your query?")
query = str(input())

if(query == 'insert'):
    #upgrade:
    '''
        create or replace procedure update(person_namee varchar, phone_numberr varchar)
        as
        $$
            begin
                UPDATE PhoneBook 
                SET phone_number = $2 
                WHERE person_name = $1;
            end;
        $$ language plpgsql;
    '''
    #insert:
    '''
        create or replace procedure insert(person_name varchar, phone_number varchar, city varchar)
        as
        $$
            begin
                insert into PhoneBook(person_name, phone_number, city) values ($1, $2, $3);
            end; 
        $$ language plpgsql;  
    '''

    print("How many people you want to add?")
    n = int(input())
    for _ in range(0,n):
        name = str(input())
        number = str(input())
        city = str(input())
        number = checkNum(number)
        if(check(name)): 
            current.execute('call insert(%s,%s,%s);', (name,number,city))
        else:
            current.execute("call update(%s, %s);",(name,number))
        

if(query == 'delete'):
    #delete:
    '''
        create or replace procedure delete(data varchar)
        as
        $$
            begin
                delete from PhoneBook where person_name = $1 or phone_number = $1; 
            end;
        $$ language plpgsql;
        call delete(%s);
    '''

    data = str(input())
    current.execute("call delete(%s);", [data])
       

if(query == 'pagination'):
    print("type your limit and offset")
    limit = int(input())
    offset = int(input())
    pa = '''
        select * from PhoneBook offset %s limit %s;
    '''
    current.execute(pa ,(limit,offset))
    print(current.fetchall())


if(query == 'query'):
    #querying:
    # '''
    #     create or replace function querying(data varchar)
    #         returns table (
    #             person_namee varchar,
    #             phone_numberr varchar,
    #             cityy varchar
    #         )
    #     as
    #     $$
    #         begin
    #             return query
    #                 select * from PhoneBook where person_name ilike $1 or phone_number ilike $1;
    #         end;
    #     $$ language plpgsql;
    # '''

    pat = str(input())
    current.execute("select querying(%s)", ["%"+pat+"%"])
    print(current.fetchall())

current.close()
config.commit()
config.close()