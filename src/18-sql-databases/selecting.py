import mysql.connector

def insert_product(name, price, image_url, description):
    # your_password: replace this with your own local MySQL password
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,image_url,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} record(s) inserted')
        print(f'id of the last inserted record: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')

def insert_products(product_list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = product_list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} record(s) inserted')
        print(f'id of the last inserted record: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')

def get_products():
    # This is where I learned the difference between fetchone() and fetchall()
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # cursor.execute('Select * From Products')
    cursor.execute('Select name,price From Products')

    # result = cursor.fetchall()
    result = cursor.fetchone()

    print(f'name: {result[0]} price: {result[1]}')

    # for product in result:
    #     # print(f'name: {product[1]} price: {product[2]}')
    #     print(f'name: {product[0]} price: {product[1]}')

get_products()
