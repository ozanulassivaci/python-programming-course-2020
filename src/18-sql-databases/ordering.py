import mysql.connector

def insert_product(name, price, image_url, description):
    # Connect to the MySQL server: host is the machine, user/password are
    # the login, database picks which database on that server to use.
    #
    # your_password: replace this with your own local MySQL password
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    # The cursor is what sends SQL statements and reads back their results.
    cursor = connection.cursor()

    # A parameterized query: %s placeholders are filled in safely by the
    # driver from `values`, instead of us pasting the values into the SQL
    # text ourselves. This is what protects against SQL injection -- a
    # malicious value can't break out of its slot and become part of the
    # SQL command.
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,image_url,description)

    cursor.execute(sql,values)

    try:
        # commit() makes the insert permanent; nothing is saved until then.
        connection.commit()
        print(f'{cursor.rowcount} record(s) inserted')
        # lastrowid is the id MySQL auto-generated for the new row.
        print(f'id of the last inserted record: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        # Catches driver-level errors so they print instead of crashing.
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')

def insert_products(product_list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = product_list

    # executemany() inserts every tuple in the list in one call.
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
    # This is where I learned that Order By can take more than one column
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # ORDER BY sorts the rows a query returns (it does NOT filter anything
    # out, and it does not change how the data is stored -- it only changes
    # the order it comes back in). By default it sorts ascending (A-Z,
    # smallest-to-largest). Listing "name, price" means: sort primarily by
    # name, and for any rows that have the same name, use price to break the
    # tie and decide their relative order.
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

    # WHERE id=%s restricts the result to the single row with that id;
    # the %s placeholder keeps the value out of the raw SQL text, which is
    # what makes this safe from SQL injection.
    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    # An id lookup can match at most one row, so fetchone() (a single tuple,
    # or None) is the appropriate call here rather than fetchall().
    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

get_products()
