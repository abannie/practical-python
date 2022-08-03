# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_month = 0
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    if payment_month < extra_payment_end_month and payment_month >= extra_payment_start_month:
        new_payment = payment + extra_payment 
        principal = principal * (1+rate/12) - new_payment 
        total_paid = total_paid + new_payment 
        payment_month += 1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid', total_paid)
