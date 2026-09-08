import pandas as pd

# pd.merge() combines two DataFrames based on matching values in a shared
# key column (much like a SQL JOIN). The commented-out block below sets up
# a classic customers/orders example to demonstrate the different join
# "how" types, before the file moves on to pd.concat() with a live example.

# customers = {
#     'CustomerId': [1,2,3,4],
#     'FirstName': ["Ahmet","Ali","Hasan","Canan"],
#     'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
# }

# Note the mismatch on purpose: orders reference CustomerId 5 and 7, which
# don't exist in the customers table above, while customers 3 and 4 have
# no orders at all -- this is exactly what makes the different join types
# behave differently.
# orders = {
#     'OrderId': [10,11,12,13],
#     'CustomerId': [1,2,5,7],
#     'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
# }

# df_customers = pd.DataFrame(customers, columns = ["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns = ["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

# how="inner" (the default) keeps ONLY rows where CustomerId exists in
# BOTH tables -- so just customers 1 and 2, who both placed a matching
# order. Customers 3/4 (no orders) and orders for 5/7 (no matching
# customer) are dropped entirely.
# result = pd.merge(df_customers,df_orders,how="inner")
# how="left" keeps EVERY row from the left table (df_customers) no matter
# what, filling in order details where a match exists and NaN where it
# doesn't -- so customers 3 and 4 would still appear, just with empty
# OrderId/OrderDate.
# result = pd.merge(df_customers,df_orders,how="left")
# how="right" is the mirror image: keeps EVERY row from the right table
# (df_orders), filling in NaN for FirstName/LastName wherever an order's
# CustomerId (5 or 7) has no matching customer.
# result = pd.merge(df_customers,df_orders,how="right")
# how="outer" keeps EVERYTHING from both tables -- every customer and
# every order -- filling NaN wherever a match is missing on either side.
# It's the union of the left and right results.
# result = pd.merge(df_customers,df_orders,how="outer")

customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Bilge","Deniz","Yılmaz","Deniz"]
}

df_customersA = pd.DataFrame(customersA, columns = ["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns = ["CustomerId","FirstName","LastName"])

# Learning note: axis=0 stacks rows, axis=1 lines dataframes up side by side.
# pd.concat() glues DataFrames together WITHOUT trying to match up any key
# column (unlike merge) -- it just stacks them along an axis you choose.
# axis=0 (the default) stacks the second DataFrame's ROWS underneath the
# first's, since both share the same column names. The result has all 8
# customers (A's 1-4 followed by B's 4-7), but note the ROW INDEX simply
# repeats (0,1,2,3,0,1,2,3) unless you pass ignore_index=True, since
# concat doesn't renumber by default -- another common gotcha.
result = pd.concat([df_customersA,df_customersB])
# axis=1 instead stacks them side by side as new COLUMNS, aligning by row
# position/index -- since both DataFrames have identical column names
# (CustomerId, FirstName, LastName) and matching row indices (0-3), this
# produces a wider table with those column names duplicated (A's three
# columns, then B's three columns) rather than merging on CustomerId
# values.
result = pd.concat([df_customersA,df_customersB],axis=1)


print(result)
