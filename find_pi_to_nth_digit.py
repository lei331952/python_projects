# Enter a number and have the program generate pi up to that many decimal places.  Keep a limit to how far the program will go.
from mpmath import mp

MAX_DECIMAL = 10000000


def get_nth_decimal_input():
    while True:
        n = int(
            input(f'How many decimal places for π (max={MAX_DECIMAL}), 0 for stop: '))
        if n <= MAX_DECIMAL and n >= 0:
            return n
        print('number is out of range, please try it again.\n')


def shell():
    while True:
        nth_decimal = get_nth_decimal_input()
        if nth_decimal == 0:
            break
        mp.dps = nth_decimal+1
        print(mp.pi)
        output = str(mp.pi)
        print(f"\nlength: {len(output)}\n")


if __name__ == '__main__':
    shell()
