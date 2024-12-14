# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number

MAX_NUMBER = 10000


def get_a_number():
    while True:
        n = int(input(f'Enter a number(max={MAX_NUMBER}), or 0 to stop: '))
        if n <= MAX_NUMBER and n >= 0:
            return n
        print('number out of range, try it again')


def get_fibonacci_sequence(n):

    assert n > 0

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def shell():
    while True:
        n = get_a_number()

        if n == 0:
            break

        fib_seq = list(get_fibonacci_sequence(n))
        print(*fib_seq)


if __name__ == "__main__":
    shell()
