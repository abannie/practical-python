# bounce.py
#
# Exercise 1.5
start_ht = 100
for i in range(10):
    new_ht = start_ht * 0.6
    i += 1
    print(f' {i} {round(new_ht, 4)}')
    start_ht = new_ht
    
