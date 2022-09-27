# report.py
#
# Exercise 2.4 (list of tuples), 2.5 (list of dict), 2.6 (dict), 2.7(apply for use case)

import csv

#Ex 2.4, 2.6
def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(holding)
    return portfolio

#Ex 2.6
def read_prices(filename):
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

def compute_networth(portfolio, stock_prices):

    networth = 0
    for stock in portfolio:
        stock_val = (stock_prices[ stock['name'] ] * stock['shares']) - (stock['shares'] * stock['price'])
        print(f"{stock['name']} today value: {stock_val}")
        networth += stock_val
    print(f'networth today: {networth}')