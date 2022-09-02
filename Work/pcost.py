# pcost.py
#
# Exercise 1.27
fname = "/home/annie/projects/practical-python/Work/Data/portfolio.csv"
with open(fname, 'rt') as f:
	headers = next(f).split(',')
	print(headers)
	total = 0.0
	for line in f:
		row = line.split(',')
		subtotal = int(row[1])*float(row[2].strip())
		print(f'{subtotal}')
		#fields = row.split(',')
		#print(fields)
		total = total + subtotal
	print(f'Total cost {total}')

