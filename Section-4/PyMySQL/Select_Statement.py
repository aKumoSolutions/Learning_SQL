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
        cursor.execute("SELECT * FROM customers")
        all = cursor.fetchone()
        print(all)


        cursor.execute("SELECT last_name FROM customers")
        lname = cursor.fetchall()
        print(lname)


        cursor.execute("SELECT first_name, phone_number FROM customers")
        name = cursor.fetchall()
        print(name)
        

    connection.close()