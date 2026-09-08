import mysql.connector

def insert_product(name, price, image_url, description):
    # Connect to the MySQL server: host is the machine, user/password log
    # us in, database picks which database on the server to use.
    #
    # your_password: replace this with your own local MySQL password
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # %s placeholders let the driver safely substitute `values` into the SQL
    # instead of us building the string ourselves -- this is what prevents
    # SQL injection (a value can't smuggle in extra SQL syntax).
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,image_url,description)

    cursor.execute(sql,values)

    try:
        # Nothing is saved to the table until commit() runs.
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

    # ORDER BY name, price sorts by name first, using price only to break
    # ties between rows that share the same name.
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

    # WHERE id=%s filters down to the single row with that id.
    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def get_product_info():
    # This is where I learned about SQL aggregate functions like COUNT, AVG, SUM, MIN, MAX
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # Aggregate functions collapse many rows down into a single summary
    # value, instead of returning one row per record like a plain SELECT
    # does:
    #   COUNT(*)     - how many rows are in the table (or match a WHERE).
    #   AVG(Price)   - the arithmetic mean of the Price column across all
    #                  matching rows.
    #   SUM(Price)   - the total of the Price column added up across all
    #                  matching rows.
    #   MIN(Price)   - the smallest Price value found.
    #   MAX(Price)   - the largest Price value found.
    # Only one of the following sql assignments is actually active (the
    # rest are commented out) -- they're left here to show the different
    # aggregate functions side by side.
    # sql = "Select COUNT(*) from Products"
    # sql = "Select AVG(Price) from Products"
    # sql = "Select SUM(Price) from Products"
    # sql = "Select MIN(Price) from Products"
    # sql = "Select MAX(Price) from Products"
    # This last query is a subquery: the inner query
    # "Select MAX(Price) from Products" runs first and produces a single
    # number (the highest price in the table); the outer query then finds
    # the Name and Price of whichever row(s) have exactly that price. This
    # is a common pattern for "give me the record that holds the max/min
    # value", since you can't put MAX(Price) directly in a WHERE clause.
    sql = "Select Name,Price from Products Where Price = (Select MAX(Price) from Products)"

    cursor.execute(sql)

    # If multiple products happen to tie for the highest price, fetchone()
    # would only return the first one MySQL happens to return -- fetchall()
    # would be needed to see every tied product.
    result = cursor.fetchone()

    print(f'result: {result[0]} {result[1]}')


get_product_info()
