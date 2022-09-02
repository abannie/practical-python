# pcost.py
#
# Exercise 1.27
fname = "/home/annie/projects/practical-python/Work/Data/portfolio.csv"
def portfolio_cost(fname):
	with open(fname, 'rt') as f:
		headers = next(f).split(',')
		print(headers)
		total = 0.0
		for line in f:
			row = line.split(',')
			try:
				subtotal = int(row[1])*float(row[2].strip())
				print(f'{subtotal}')
				total = total + subtotal
			except ValueError:
				print("couldn't parse", row)

		return total
		#print(f'Total cost {total}')

cost = portfolio_cost(fname)
print('Total cost:', cost)