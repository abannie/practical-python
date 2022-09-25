# report.py
#
# Exercise 2.4

import csv

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

def read_prices(filename):
    '''read (current) prices of stock'''

    portfolio = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            print(row)
            if row:
                portfolio[row[0]] = float(row[1])
            else:
                print("read prices row error", row)
    return portfolio
