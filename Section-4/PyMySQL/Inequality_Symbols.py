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
        cursor.execute("SELECT * FROM products WHERE price < 3.00")
        sort = cursor.fetchall()
        print(sort)

    
    connection.close()
