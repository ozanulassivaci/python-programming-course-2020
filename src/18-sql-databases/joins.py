import mysql.connector

def insert_product(name, price, image_url, description):
    # Connect to the MySQL server on this machine, log in as root, and work
    # against the "node_app" database.
    #
    # your_password: replace this with your own local MySQL password
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # %s placeholders keep the actual values separate from the SQL text, so
    # the driver can substitute them safely -- this is what prevents SQL
    # injection.
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
    # This is where I learned the difference between a plain join and an INNER JOIN with table aliases
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # A JOIN combines rows from two (or more) tables into one result, based
    # on a relationship between them -- here, each product belongs to a
    # category, and Products.Categoryid stores the id of the matching row in
    # the Categories table (this is called a "foreign key").
    #
    # An INNER JOIN returns only the rows that have a match in BOTH tables:
    # if a product's Categoryid doesn't match any row in Categories (or vice
    # versa), that row is left out of the result entirely. (This is the
    # default kind of join in SQL when you just write "join" with no
    # qualifier -- MySQL treats plain "join" as INNER JOIN.) This is
    # different from a LEFT JOIN, which would keep every product even if it
    # has no matching category (filling in NULLs for the missing category
    # columns), or a RIGHT JOIN, which would keep every category even if no
    # product uses it.
    #
    # "on Categories.id=Products.Categoryid" is the join condition: it tells
    # SQL which column in each table identifies "the same relationship" --
    # i.e. match up each product with the category whose id equals that
    # product's Categoryid.
    #
    # "as p" and "as c" below are table aliases: short nicknames for
    # Products and Categories so the rest of the query can write p.name
    # instead of the longer Products.name. This becomes especially handy
    # once column names (like "name") exist in more than one of the joined
    # tables and SQL needs to know which table's "name" you mean.
    #
    # Only the last of these is actually executed -- the earlier ones are
    # commented out and shown here to build up the idea step by step:
    # sql = "Select * From Products"
    # sql = "Select * From Categories"
    # sql = "Select * From Products inner join Categories on Categories.id=Products.Categoryid"
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid"
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid where Categories.name='Telefon'"
    sql = "Select p.name,p.price,c.name From Products as p inner join Categories as c on c.id=p.Categoryid where p.name='Samsung s8'"


    cursor.execute(sql)

    try:
        result = cursor.fetchall()
        for product in result:
            print(product)

    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')

def get_product_by_id(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # WHERE id=%s narrows the SELECT down to the one row with that id.
    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def update_product(id, name, price):
    connection = mysql.connector.connect(host="localhost", user = "root", password="your_password", database="node_app")
    cursor = connection.cursor()

    # UPDATE changes existing rows instead of adding new ones. "Set name=,
    # price=" lists which columns to overwrite and with what, and "where
    # id=" restricts the change to just the one row matching that id -- if
    # this WHERE clause were left off, EVERY row in the table would be
    # updated.
    sql = "Update products Set name= %s, price= %s where id= %s"
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        # As with INSERT, the change only becomes permanent after commit().
        connection.commit()
        print(f'{cursor.rowcount} record(s) updated')
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection closed.')

get_products()
