# username, password => database

# 'ozanulassivaci' , '123456'

# Comparison operators always produce a bool (True or False) -- they never
# change any of the values being compared, they just answer a yes/no
# question about them.
a, b, c, d = 5, 5, 10, 4

password = '1234'
username = 'ozanulassivaci'

result = (a == b)  # True   -- "==" checks equality: 5 equals 5
result = (a == c)  # False  -- 5 does not equal 10
result = ('sdktrn' == username)          # False -- different text
result = ('ozanulassivaci' == username)  # True  -- identical text
result = (a != b)  # False  -- "!=" is "not equal"; 5 IS equal to 5
result = (a != c)  # True   -- 5 is not equal to 10
result = (a > c)   # False  -- 5 is not greater than 10
result = (a < c)   # True   -- 5 is less than 10
result = (a >= b)  # True   -- ">=" is "greater than or equal to"; 5>=5 holds
result = (c <= b)  # False  -- "<=" is "less than or equal to"; 10<=5 does not hold
# Booleans are secretly integers under the hood: True behaves as 1 and
# False behaves as 0, so comparing a bool to the matching int with "=="
# is True.
result = (True == 1)   # True
result = (False == 0)  # True
# Because bools act as 0/1 in arithmetic, this isn't string concatenation
# or anything special -- it's plain addition: False + True + 40
#   ->    0   +   1   + 40  = 41
result = False + True + 40

print(result)  # 41
