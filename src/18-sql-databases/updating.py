import mysql.connector

def insert_product(name, price, image_url, description):
    # Connect to the MySQL server on this machine, log in as root, and use
    # the "node_app" database.
    #
    # your_password: replace this with your own local MySQL password
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # %s placeholders let the driver substitute `values` safely, instead of
    # us building the SQL string by hand -- the standard way to avoid SQL
    # injection.
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,image_url,description)

    cursor.execute(sql,values)

    try:
        # The insert only becomes permanent once commit() runs.
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

    # executemany() inserts every tuple in product_list with one call.
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

    # ORDER BY name, price sorts alphabetically by name, using price only to
    # break ties when two rows share the same name.
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

    # WHERE id=%s filters the SELECT down to just the one row with this id.
    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def update_product(id, name, price):
    # This is where I learned that an UPDATE without a WHERE clause changes every row in the table
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # UPDATE modifies rows that already exist (as opposed to INSERT, which
    # adds new ones). "Set name=, price=" says which columns to overwrite
    # and with what new values, and "where id=" limits the change to only
    # the row whose id matches -- this WHERE clause is what keeps the update
    # scoped to a single product. If it were left off entirely, MySQL would
    # happily set name and price on every single row in the Products table,
    # which is the mistake the comment above is warning about.
    sql = "Update products Set name= %s, price= %s where id= %s"
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        # Like INSERT, an UPDATE isn't permanent until commit() is called.
        connection.commit()
        # rowcount here tells you how many rows actually matched the WHERE
        # clause and got updated (0 if no row had that id).
        print(f'{cursor.rowcount} record(s) updated')
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')

update_product(1, 'Iphone 8', 6000)
get_products()
