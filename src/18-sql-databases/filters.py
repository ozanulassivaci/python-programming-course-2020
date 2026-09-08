import mysql.connector

def insert_product(name, price, image_url, description):
    # mysql.connector.connect(...) logs into a MySQL server: host is which
    # machine it's running on ("localhost" = this computer), user/password
    # are the login credentials, and database picks which database on that
    # server ("node_app") to use.
    #
    # your_password: replace this with your own local MySQL password
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    # A cursor is what you use to send SQL and read back results over the
    # connection.
    cursor = connection.cursor()

    # A parameterized query: the %s placeholders get filled in with `values`
    # by the driver, rather than us pasting the values into the SQL string
    # ourselves. This protects against SQL injection -- if a value (say, a
    # product name) contained SQL-looking text like  '); DROP TABLE Products;--
    # a hand-built string could accidentally execute it as a command, but a
    # placeholder always treats it as plain data.
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,image_url,description)

    cursor.execute(sql,values)

    try:
        # Nothing is permanently written until commit() is called.
        connection.commit()
        # rowcount = how many rows were affected (1 for a single insert).
        print(f'{cursor.rowcount} record(s) inserted')
        # lastrowid = the auto-generated id MySQL assigned to the new row.
        print(f'id of the last inserted record: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        # Catch driver-level errors (bad SQL, constraint violations, etc.)
        # so a failure prints a message instead of crashing the script.
        print('error:', err)
    finally:
        # Always close the connection, success or failure, to avoid leaving
        # it open.
        connection.close()
        print('database connection closed.')

def insert_products(product_list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = product_list

    # executemany() runs the same INSERT once per tuple in the list, so many
    # rows can be inserted with a single call instead of looping execute().
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

    # "Select * From Products" reads every column for every row in the
    # Products table -- no filtering, no restrictions yet.
    cursor.execute("Select * From Products")

    result = cursor.fetchall()

    for product in result:
        print(f'id: {product[0]} name: {product[1]} price: {product[2]}')

def get_product_by_id(id):
    # This is where I learned to filter rows with a WHERE clause instead of pulling back the whole table
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # WHERE narrows down which rows a SELECT (or UPDATE/DELETE) applies to.
    # Without it, "Select * From Products" would return every row; with
    # "Where id=%s" it only returns the one row whose id column matches the
    # value we pass in. Using %s here (rather than gluing `id` into the
    # string) keeps this safe from SQL injection, the same reason INSERT
    # uses placeholders above.
    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    # Since a primary-key id can only match at most one row, fetchone() is
    # the right choice here -- we know there's zero or one result, so there's
    # no need for fetchall()'s list of many rows.
    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')
