'''
Ask the user to enter 2 integers a and b
output a^b: pow(a,b) in O(lg n) time complexity
'''


def power(a, b):
    result = 1
    base = a
    while b > 0:
        if b % 2 == 1:
            result *= base

        base *= base

        b //= 2

    return result


def power2(a, b):
    result = 1
    for _ in range(b):
        result *= a

    return result


print(power(2, 10))
print(power2(2, 10))
