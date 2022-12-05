# report.py
#
# Exercise 2.4 (list of tuples), 2.5 (list of dict), 2.6 (dict), 2.7(apply for use case), 2.9 (collecting data)

import csv

#Ex 2.4, 2.6
def read_portfolio(filename)->list:
    '''Computes the total cost (shares*price) of a portfolio file
	returns list of stocks stored by (name, share_num, price)'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(holding)
    return portfolio

#Ex 2.6
def read_prices(filename)->dict:
    '''read (current) prices of stock'''

    stocks = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            print(row)
            if row:
                stocks[row[0]] = float(row[1])
            else:
                print("read prices row error", row)
    return stocks

#ex 2.7
def compute_networth(portfolio, stock_prices)->None:

    networth = 0
    for stock in portfolio:
        stock_val = (stock_prices[ stock['name'] ] * stock['shares']) - (stock['shares'] * stock['price'])
        print(f"{stock['name']} today value: {stock_val}")
        networth += stock_val
    print(f'networth today: {networth}')

#ex 2.9 create a table of stock, shares and price changes
def make_report(portfolio:list, stock_prices:dict)->list:

    stock_rows = []
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        today_price = stock_prices[name]
        change = stock['price'] - today_price
        print(f"{name}, {shares},today price: {today_price}, {change}")
        stock_row = (name, shares, today_price, change)
        print(stock_row)
        stock_rows.append(stock_row)
    return stock_rows 

