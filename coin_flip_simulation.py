'''
Simulate flipping a single coin however many times the user decides.
Record the outcomes
and count the number of tails and heads'''

import random
from collections import Counter

while True:
    flips = int(input('How many times to flip a coin(0 to quit): '))
    if flips == 0:
        break

    trace = []
    for _ in range(flips):
        trace.append(random.randint(0, 1))

    print(trace)
    counter = Counter(trace)
    print(f"Heads: {counter[0]}, Tails:{counter[1]}")
