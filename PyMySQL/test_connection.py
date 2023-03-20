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


# if connection:
#     with connection.cursor() as cursor:
        # cursor.execute("INSERT INTO test (id, LastName, FirstName, DepartmentCode) VALUES (3, 'Osmonaliev', 'Izar', 2), (3, 'Absatarov', 'Daniel', 3)")
        
        # cursor.execute("SELECT * FROM test")
        # result = cursor.fetchall()
        # print(result)
        



