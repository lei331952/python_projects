# Have the program find prime numbers until the user chooses to stop asking for the next one.
from math import sqrt
from sympy import isprime


def is_prime_for_odd_number(n):
    for divisor in range(3, int(sqrt(n)+1), 2):
        if n % divisor == 0:
            return False

    return True


def get_next_prime_number():
    yield 2
    n = 3
    while True:
        if is_prime_for_odd_number(n):
            yield n
        n += 2


def get_next_prime_number_option2():
    yield 2
    n = 3
    while True:
        if isprime(n):
            yield n
        n += 2


def main():
    print("Press Enter to generate next prime number, 's' to stop.")

    gen = get_next_prime_number_option2()
    while True:
        ans = input()

        if ans == 's':
            break
        else:
            print(next(gen))


if __name__ == "__main__":
    main()
