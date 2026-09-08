import mysql.connector

def insert_product(name, price, image_url, description):
    # Connect to the MySQL server: host/user/password log us in, database
    # picks which database on the server ("node_app") to work with.
    #
    # your_password: replace this with your own local MySQL password
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # %s placeholders are filled in safely by the driver from `values`,
    # instead of being pasted into the SQL text -- this is what prevents SQL
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

    # executemany() inserts every tuple in product_list with a single call.
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

    # ORDER BY name, price sorts by name first, using price to break ties.
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

    # WHERE id=%s restricts the SELECT to the single row with this id.
    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def update_product(id, name, price):
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # UPDATE overwrites the name and price columns, but only on the row
    # whose id matches -- the WHERE clause is what keeps this scoped to one
    # product instead of the whole table.
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

    # DELETE removes entire rows from a table. Just like UPDATE, the WHERE
    # clause is what limits the damage to a single row -- "where id=%s"
    # means only the row with that exact id is removed. If this query were
    # written as just "delete from products" with no WHERE at all, MySQL
    # would delete every single row in the table, with no undo (short of
    # restoring from a backup) once it's committed.
    sql = "delete from products where id=%s"
    values = (id,)
    cursor.execute(sql,values)

    try:
        # As with INSERT/UPDATE, the delete is only permanent after commit().
        connection.commit()
        # rowcount tells you how many rows actually matched and were removed.
        print(f'{cursor.rowcount} record(s) deleted')
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')


delete_product(5)
get_products()
