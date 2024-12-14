from collections import Counter


def total_distance_concise(list1: list[int], list2: list[int]):
    list1.sort()
    list2.sort()
    return sum([abs(x-y) for x, y in zip(list1, list2)])


def total_distance(list1: list[int], list2: list[int]):

    list1.sort()
    list2.sort()

    distance: list[int] = []

    for index in range(len(list1)):
        distance.append(abs(list1[index]-list2[index]))

    return sum(distance)


def process_file(file_path: str):
    list1: list[int] = []
    list2: list[int] = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Strip whitespace and split the line into numbers
                numbers = list(map(int, line.strip().split()))
                if len(numbers) >= 2:  # Ensure at least two numbers exist in the line
                    list1.append(numbers[0])
                    list2.append(numbers[1])
                else:
                    print(f"Skipping line (not enough numbers): {
                          line.strip()}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as e:
        print(f"Error processing file: {e}")

    return list1, list2


file_path = "input.txt"
list1, list2 = process_file(file_path)


# print(total_distance(list1, list2))

list1_example = [3, 4, 2, 1, 3, 3]
list2_example = [4, 3, 5, 3, 9, 3]


def total_similarityscore(list1: list[int], list2: list[int]):

    similarity_score: list[int] = []

    for index in range(len(list1)):
        similarity_score.append(list1[index] * list2.count(list1[index]))
    # print(similarity_score)

    return sum(similarity_score)


print(total_similarityscore(list1, list2))

# an elegant approach with generator and Counter

a, b = [], []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split())
        a.append(x)
        b.append(y)

a.sort()
b.sort()
n = len(a)

# part 1
print(sum(abs(a[i]-b[i]) for i in range(n)))

# part 2
c = Counter(b)
print(sum(a[i]*c[a[i]] for i in range(n)))
