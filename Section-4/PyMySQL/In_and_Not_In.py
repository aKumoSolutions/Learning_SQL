import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='burkanov-e',
        password='passwd',
        db='coffee_store',
        autocommit=True
        )
except:
    print("not working")


if connection:
    with connection.cursor() as cursor: 
        cursor.execute("SELECT * FROM customers WHERE first_name NOT IN ('Katie', 'John', 'George')")
        sort = cursor.fetchall()
        print(sort)

        cursor.execute("SELECT * FROM customers WHERE last_name IN ('Taylor', 'Bluth', 'Armstrong')")
        sort = cursor.fetchall()
        print(sort)


    connection.close()
