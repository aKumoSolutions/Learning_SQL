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
    print('not working')


if connection:
    with connection.cursor() as cursor:
        cursor.execute('''SELECT name, price FROM products WHERE coffee_origin IN ('Colombia', 'Indonesia')
ORDER BY name ASC''')
        sort = cursor.fetchall()
        print(sort)


        cursor.execute('''SELECT * FROM orders WHERE order_time BETWEEN '2017-02-01' AND '2017-02-28' 
AND customer_id IN (2,4,6,8) ORDER BY order_time ASC''')
        sort1 = cursor.fetchall()
        print(sort1)


        cursor.execute('''SELECT first_name, phone_number, last_name FROM customers 
WHERE last_name LIKE "%ar%"''')
        sort2 = cursor.fetchall()
        print(sort2)


    connection.close()