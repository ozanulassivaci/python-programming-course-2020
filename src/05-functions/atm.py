# ATM Application

ozan_account = {
    'name': 'Ozan Ulas Sivaci',
    'account_number': '13245678',
    'balance': 3000,
    'overdraft_limit': 2000
}

aykut_account = {
    'name': 'Aykut Yilmaz',
    'account_number': '12345678',
    'balance': 2000,
    'overdraft_limit': 1000
}

# Dicts (like lists) are mutable reference types: when `account` is
# passed into this function, the parameter points at the SAME dict
# object the caller passed in -- not a copy. So every mutation made here
# (account['balance'] -= amount, etc.) is permanently visible on the
# original dict too, even after the function returns. This is the same
# reference-semantics idea explored with lists in
# 01-python-objects-and-data-structures/reference.py, just applied to a
# dict this time.
def withdraw_money(account, amount):
    print(f"Hello {account['name']}")

    # Simple case: there's enough in the regular balance alone.
    if (account['balance'] >= amount):
        account['balance'] -= amount
        print('you can take your money.')
        check_balance(account)
    else:
        # Not enough in the balance alone -- check if the balance PLUS
        # the overdraft limit together would cover the request.
        total = account['balance'] + account['overdraft_limit']

        if (total >= amount):
            use_overdraft = input('use the overdraft limit (y/n)')

            if use_overdraft == 'y':
                # How much of the withdrawal has to come out of the
                # overdraft, since the balance alone can't cover it all.
                overdraft_amount = amount - account['balance']
                account['balance'] = 0
                account['overdraft_limit'] -= overdraft_amount
                print('you can take your money.')
                check_balance(account)
            else:
                print(f"account {account['account_number']} has a balance of {account['balance']}.")
        else:
            # Even balance + overdraft isn't enough to cover the request.
            print('sorry, insufficient balance')
            check_balance(account)


def check_balance(account):
    print(f"account {account['account_number']} has a balance of {account['balance']} TL. Your overdraft limit is {account['overdraft_limit']} TL.")

# ozan_account starts with balance=3000. Withdrawing exactly 3000 hits the
# first branch (balance >= amount is True, 3000 >= 3000), leaving balance
# at 0 afterward. Because dicts are mutated in place, this change to
# ozan_account['balance'] persists after the function call returns.
withdraw_money(ozan_account, 3000)

print('*****************')

# By now ozan_account['balance'] is 0 (from the call above), so this
# withdrawal request of 2000 fails the first check (0 >= 2000 is False)
# and falls into the overdraft branch: total = 0 + 2000 = 2000, which is
# exactly enough (2000 >= 2000), so the user is asked whether to use the
# overdraft.
withdraw_money(ozan_account, 2000)
