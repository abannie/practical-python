# pcost.py
#
# Exercise 1.27
# pcost.py
import os
import sys


def portfolio_cost(fname):
    with open(fname, 'rt') as f:
        headers = next(f).split(',')
        print(headers)
        total = 0.0
        for line in f:
            row = line.split(',')
            try:
                subtotal = int(row[1]) * float(row[2].strip())
                print(f'{subtotal}')
                total = total + subtotal
            except ValueError:
                print("couldn't parse", row)

        return total


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = os.getcwd() + "/Data/portfolio.csv"
    cost = portfolio_cost(filename)
    print('Total cost:', cost)
