import mysql.connector

def insert_product(name, price, image_url, description):
    # mysql.connector.connect(...) opens a fresh connection to the MySQL
    # server for this one function call. host/user/password identify which
    # server and account to log in as (like logging into a website), and
    # database picks which database on that server to work with ("node_app"
    # here). Opening a brand-new connection inside every function is not the
    # most efficient pattern (a real app would usually share one connection
    # or a pool of them), but it keeps each function in this file fully
    # self-contained and easy to read in isolation.
    #
    # your_password: replace this with your own local MySQL password
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    # A cursor is the object you actually send SQL through and read results
    # from -- the connection is the open line to the database, the cursor is
    # what you use to "speak" on it.
    cursor = connection.cursor()

    # This is a parameterized query: instead of pasting name/price/etc.
    # directly into the SQL text, we write %s placeholders and pass the real
    # values separately in a tuple. The database driver substitutes them
    # safely, escaping anything that could otherwise be interpreted as SQL
    # syntax. This matters because if we instead built the string ourselves
    # (e.g. f"...VALUES ('{name}', ...)"), a value like  O'Brien'); DROP TABLE Products;--
    # typed by a user could break out of the intended string and run its own
    # SQL commands -- an attack called SQL injection. Placeholders make that
    # impossible because the driver always treats the substituted values as
    # plain data, never as SQL code.
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,image_url,description)

    # cursor.execute(sql, values) sends the INSERT statement to the server,
    # with `values` filled into the %s placeholders in order.
    cursor.execute(sql,values)

    try:
        # INSERT/UPDATE/DELETE statements only take effect once you call
        # connection.commit(). Until then, the change lives in an uncommitted
        # transaction and could still be rolled back / discarded. This gives
        # you a chance to run several related statements and only make them
        # permanent together.
        connection.commit()
        # cursor.rowcount tells you how many rows were affected by the last
        # statement -- for a single INSERT that's normally 1.
        print(f'{cursor.rowcount} record(s) inserted')
        # cursor.lastrowid is the auto-generated primary key (e.g. an AUTO_
        # INCREMENT id) that MySQL assigned to the row we just inserted.
        print(f'id of the last inserted record: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        # mysql.connector.Error is the base class for errors the MySQL
        # driver can raise (bad SQL syntax, constraint violations, a lost
        # connection, etc.). Catching it here means a failed insert prints a
        # friendly message instead of crashing the whole program.
        print('error:', err)
    finally:
        # `finally` runs whether or not an error happened above, so the
        # connection always gets closed and we don't leak open connections
        # to the database server.
        connection.close()
        print('database connection closed.')

def insert_products(product_list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = product_list

    # executemany() runs the same parameterized SQL once per tuple in
    # `values`, which lets you insert many rows in one call instead of
    # looping and calling execute() over and over -- both less code and
    # generally faster, since the driver can batch the work.
    cursor.executemany(sql,values)

    try:
        connection.commit()
        # Here rowcount reflects the total number of rows inserted by the
        # whole batch, not just one.
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

    # SELECT reads data without changing it. "name,price" after SELECT means
    # "only give me these two columns", not every column in the table --
    # useful when you don't need the rest of the row and want to send less
    # data back over the network.
    # cursor.execute('Select * From Products')
    cursor.execute('Select name,price From Products')

    # fetchall() would return every matching row as a list of tuples.
    # fetchone() instead returns just the NEXT single row from the result
    # (here, the first one, since nothing's been fetched yet) as one tuple,
    # or None if there are no more rows. Use fetchone() when you only need
    # one record, or when you want to process a large result set row-by-row
    # without loading it all into memory at once.
    # result = cursor.fetchall()
    result = cursor.fetchone()

    # Since we selected "name,price" in that order, result[0] is the name
    # and result[1] is the price of that single row.
    print(f'name: {result[0]} price: {result[1]}')

    # This commented-out block shows what looping would look like if we had
    # used fetchall() instead -- `result` would then be a list of tuples,
    # and this loop would print every row instead of just one.
    # for product in result:
    #     # print(f'name: {product[1]} price: {product[2]}')
    #     print(f'name: {product[0]} price: {product[1]}')

get_products()
