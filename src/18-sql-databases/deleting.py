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
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    cursor.execute("Select * From Products Order By name, price")

    try:
        result = cursor.fetchall()
        for product in result:
            print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')

def get_product_by_id(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def update_product(id, name, price):
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    sql = "Update products Set name= %s, price= %s where id= %s"
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} record(s) updated')
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')

def delete_product(id):
    # This is where I first understood how a WHERE clause protects the rest of the table when deleting
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    sql = "delete from products where id=%s"
    values = (id,)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} record(s) deleted')
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')


delete_product(5)
get_products()
