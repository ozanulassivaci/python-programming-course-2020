username = 'ozanulassivaci'
password = '1234'

# The outer if checks the username first. Since username really is
# 'ozanulassivaci', this condition is True, so Python enters this block
# and evaluates the nested if next (the else on line 12 is skipped
# entirely).
if (username == 'ozanulassivaci'):

    # The inner if compares the actual password ('1234') against the
    # literal '12345' -- these are NOT equal (there's an extra '5'), so
    # this condition is False, and control falls through to the nested
    # else below. With these exact values, this program will always
    # print 'wrong password', never 'Welcome'.
    if (password == '12345'):
        print('Welcome')
    else:
        print('wrong password')

else:
    print('wrong username')
