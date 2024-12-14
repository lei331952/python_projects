'''
A happy number is defined by the following process.  Starting with any positive integer, 
replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1(where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Theose numbers for which this process ends in 1 are happy numbers, 
while those that do not end in 1 are unhappy numbers.  Find first 8 happy numbers.
'''
from functools import reduce

total_to_be_found = 8
# fmt: off
square_sum_of_digits = lambda n_str: reduce(lambda acc, x: acc + int(x)**2, n_str, 0)
# fmt: on
found = 0
for n in range(1, 100):
    n_str = str(n)
    print(n_str)
    seq = [n]
    for _ in range(200):
        new_n = square_sum_of_digits(n_str)
        seq.append(new_n)
        if new_n == 1:
            print(f"Found Happy Number, Sequence: {seq}")
            found += 1
            break
        n_str = str(new_n)
    if found == total_to_be_found:
        break
