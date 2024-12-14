# Have the user enter a number and find all Prime Factors (if there are any) and display them.

def get_a_number():
    return int(input('Enter a number (0 to stop): '))


def get_all_prime_factors(n):
    if n < 2:
        return {}

    factors = {}
    divisor = 2

    while n % divisor == 0:
        factors[divisor] = factors.get(divisor, 0) + 1
        n //= divisor

    divisor = 3

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        divisor += 2

    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return factors


def main():
    while True:
        n = get_a_number()

        if n == 0:
            break

        factors = get_all_prime_factors(n)

        print(factors)


if __name__ == "__main__":
    main()
