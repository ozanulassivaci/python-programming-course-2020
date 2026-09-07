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

def withdraw_money(account, amount):
    print(f"Hello {account['name']}")

    if (account['balance'] >= amount):
        account['balance'] -= amount
        print('you can take your money.')
        check_balance(account)
    else:
        total = account['balance'] + account['overdraft_limit']

        if (total >= amount):
            use_overdraft = input('use the overdraft limit (y/n)')

            if use_overdraft == 'y':
                overdraft_amount = amount - account['balance']
                account['balance'] = 0
                account['overdraft_limit'] -= overdraft_amount
                print('you can take your money.')
                check_balance(account)
            else:
                print(f"account {account['account_number']} has a balance of {account['balance']}.")
        else:
            print('sorry, insufficient balance')
            check_balance(account)


def check_balance(account):
    print(f"account {account['account_number']} has a balance of {account['balance']} TL. Your overdraft limit is {account['overdraft_limit']} TL.")

withdraw_money(ozan_account, 3000)

print('*****************')

withdraw_money(ozan_account, 2000)
