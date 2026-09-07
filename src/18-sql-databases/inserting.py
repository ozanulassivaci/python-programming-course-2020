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


# This is where I practiced collecting several records from the user before writing them all at once with executemany
product_list = []
while True:
    name = input('product name: ')
    price = float(input('product price: '))
    image_url = input('product image name: ')
    description = input('product description: ')

    product_list.append((name, price, image_url, description))

    result = input('do you want to continue? (y/n)')
    if result == 'n':
        print('Saving your records to the database...')
        print(product_list)
        insert_products(product_list)
        break

# insert_product(name, price, image_url, description)
