import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='burkanov-e',
        password='T821981f',
        db='coffee_store',
        autocommit=True
        )
except:
    print("not working")


if connection:
    with connection.cursor() as cursor: 
        cursor.execute("SELECT * FROM customers WHERE phone_number IS NOT NULL") 
        sort = cursor.fetchall()
        print(sort)

        cursor.execute("SELECT * FROM customers WHERE phone_number IS NULL") 
        sort1 = cursor.fetchall()
        print(sort1)


    connection.close()
