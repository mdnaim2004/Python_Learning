balance = 3000 # global variable.....

def buy_things(items, price):
    # local scope variable
    # you csn sccess  global variable useing the global keyword
    global balance
    # if you want to modify a global variable, you have to use the global keyword
    print(f'previous balance value', balance)

    # balance = 500 # local variable
    balance = balance - price
    print(f'balance after buying{items}', balance)

buy_things('sunglass', 1000)