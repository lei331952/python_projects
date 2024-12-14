from mpmath import mp


def get_num_digits():
    n = int(input('num of digits for e(0 to stop): '))
    return n


def getELoop():
    while True:
        nth = get_num_digits()
        if nth == 0:
            break
        mp.dps = nth + 1
        print(mp.e)

        print(f"length: 10{len(str(mp.e))}\n")


if __name__ == "__main__":
    getELoop()
