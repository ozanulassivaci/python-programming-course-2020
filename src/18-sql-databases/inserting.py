import mysql.connector

def insert_product(name, price, image_url, description):
    # Connect to MySQL: host/user/password log us into the server, database
    # picks which database on that server to use ("node_app").
    #
    # your_password: replace this with your own local MySQL password
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # A parameterized INSERT: the %s placeholders are filled in from
    # `values` by the driver rather than by string-concatenating them into
    # the SQL text ourselves. This is the standard defense against SQL
    # injection -- a value containing SQL-looking characters (quotes,
    # semicolons, etc.) is still treated as plain data, never as part of the
    # command.
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,image_url,description)

    cursor.execute(sql,values)

    try:
        # Nothing is actually written to the table until commit() is called.
        connection.commit()
        # rowcount = number of rows the last statement affected.
        print(f'{cursor.rowcount} record(s) inserted')
        # lastrowid = the id MySQL auto-generated for the newly inserted row.
        print(f'id of the last inserted record: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        # Catches database errors (bad SQL, constraint violations, etc.) so
        # the script reports them instead of crashing.
        print('error:', err)
    finally:
        # Always release the connection, whether or not it succeeded.
        connection.close()
        print('database connection closed.')


def insert_products(product_list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = product_list

    # executemany() runs the same parameterized INSERT once per tuple in
    # product_list, inserting many rows with a single call instead of
    # looping over execute() ourselves.
    cursor.executemany(sql,values)

    try:
        connection.commit()
        # Here rowcount is the total number of rows inserted across the
        # whole batch.
        print(f'{cursor.rowcount} record(s) inserted')
        print(f'id of the last inserted record: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')


# This is where I practiced collecting several records from the user before writing them all at once with executemany
#
# This loop asks the user, over and over, to type in one product's details,
# builds a tuple of those four values, and appends it to product_list. When
# the user finally answers 'n' to "continue?", the whole list of tuples is
# handed to insert_products() in one shot, so all the rows are inserted
# together via executemany() rather than one INSERT per product.
product_list = []
while True:
    name = input('product name: ')
    # float() converts the typed text (a string) into a decimal number,
    # since prices need to support fractional values like 19.99.
    price = float(input('product price: '))
    image_url = input('product image name: ')
    description = input('product description: ')

    # Each product becomes one tuple, in the same column order the SQL
    # statement expects (name, price, imageUrl, description).
    product_list.append((name, price, image_url, description))

    result = input('do you want to continue? (y/n)')
    if result == 'n':
        print('Saving your records to the database...')
        print(product_list)
        insert_products(product_list)
        break

# insert_product(name, price, image_url, description)
