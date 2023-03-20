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
        cursor.execute("SELECT * FROM products WHERE coffee_origin = 'Colombia';")
        sort1 = cursor.fetchall()
        print(sort1)

        cursor.execute("SELECT * FROM products WHERE price = 3.00 AND coffee_origin = 'Colombia';")
        sort2 = cursor.fetchall()
        print(sort2)

        cursor.execute("SELECT * FROM products WHERE price = 3.00 OR coffee_origin = 'Colombia';")
        sort3 = cursor.fetchall()
        print(sort3)

