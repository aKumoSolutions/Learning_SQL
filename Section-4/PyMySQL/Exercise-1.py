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
        cursor.execute("SELECT first_name, phone_number FROM customers WHERE gender = 'F' AND last_name = 'Bluth'") 
        sort = cursor.fetchall()
        print(sort)

        cursor.execute("SELECT name FROM products WHERE price > 3.00 OR coffee_origin = 'Sri Lanka'") 
        sort1 = cursor.fetchall()
        print(sort1)

        cursor.execute("SELECT * FROM customers WHERE gender = 'M' AND phone_number IS NULL") 
        sort2 = cursor.fetchall()
        print(sort2)

        
    connection.close()
