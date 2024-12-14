from functools import reduce


# fmt: off
factorial = lambda n: reduce(lambda x,y:x*y, range(1,n+1)) if n>1 else 1
# fmt: on


def factorial_calculator_easier_to_understand(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def main():

    while True:
        n = int(input('Enter a number(0 to stop): '))
        if n == 0:
            break
        print(f"{n}! = {factorial(n)}")


if __name__ == "__main__":
    main()
