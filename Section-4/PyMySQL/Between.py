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
        cursor.execute('''SELECT product_id, customer_id, order_time FROM orders 
        WHERE order_time BETWEEN "2017-01-01" AND "2017-01-07"''')

        sort = cursor.fetchall()
        print(sort)

        cursor.execute('''SELECT product_id, customer_id, order_time FROM orders 
        WHERE order_time BETWEEN "2017-01-01" AND "2017-01-07"''')
        sort1 = cursor.fetchall()
        print(sort1) 

    connection.close()